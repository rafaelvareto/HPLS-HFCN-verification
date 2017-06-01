import argparse
import cv2 as cv
import itertools
import matplotlib
import numpy as np
import pickle
import random

matplotlib.use('Agg')

from auxiliar import generate_pos_neg_dict
from auxiliar import generate_precision_recall, plot_precision_recall
from auxiliar import generate_roc_curve, plot_roc_curve
from auxiliar import iteration_to_fold
from auxiliar import learn_plsh_model, learn_plsh_v_model
from auxiliar import load_txt_file, read_fold_file
from auxiliar import mount_tuple
from auxiliar import split_into_chunks
from joblib import Parallel, delayed
from pls_classifier import PLSClassifier

parser = argparse.ArgumentParser(description='HPLS for Face Verification with NO Feature Extraction')
parser.add_argument('-p', '--path', help='Path do binary feature file', required=False, default='./features/')
parser.add_argument('-c', '--collection', help='Input file name containing folds', required=False, default='./datasets/lfw/lfw_pairs.txt')
parser.add_argument('-d', '--dataset', help='Dataset name', required=False, default='lfw')
parser.add_argument('-f', '--features', help='Input containing binary FEATURES_TEST', required=False, default='LFW-DEEP.bin')
parser.add_argument('-hm', '--hash_models', help='Number of hash functions', required=False, default=100)
parser.add_argument('-hs', '--hash_samples', help='Number of samples per hash model', required=False, default=100)
parser.add_argument('-it', '--iterations', help='Number of executions', required=False, default=1)
args = parser.parse_args()

PATH = str(args.path)
COLLECTION = str(args.collection)
DATASET = str(args.dataset)
FEATURES = str(args.features) 
HASH_MODELS = int(args.hash_models)
HASH_SAMPLES = int(args.hash_samples)
ITERATIONS = int(args.iterations)
FEAT_SET = FEATURES.replace('-DEEP.bin', '') 
OUTPUT_NAME = 'HPLS_VC_' + FEAT_SET + '_' + str(HASH_MODELS) + '_' + str(HASH_SAMPLES) + '_' + str(ITERATIONS)


def main():
    prs = []
    rocs = []
    with Parallel(n_jobs=-2, verbose=11, backend='multiprocessing') as parallel_pool:
        for index in range(ITERATIONS):
            print('ITERATION #%s' % str(index+1))
            pr, roc = hplsfacev(args, parallel_pool)
            prs.append(pr)
            rocs.append(roc)
            
            prs_f, rocs_f = iteration_to_fold(prs, rocs)
            with open('./files/' + OUTPUT_NAME + '.file', 'w') as outfile:
                pickle.dump([prs_f, rocs_f], outfile)
            for index in range(len(prs_f)):
                plot_precision_recall(prs_f[index], OUTPUT_NAME + '_fold_' + str(index + 1))
            for index in range(len(rocs_f)):
                plot_roc_curve(rocs_f[index], OUTPUT_NAME + '_fold_' + str(index + 1))


def hplsfacev(args, parallel_pool):
    print('>> LOADING DATASET FOLDS')
    pos_folds, neg_folds = read_fold_file(COLLECTION)
    assert len(pos_folds) == len(neg_folds)
    
    print('>> LOADING DATASET FEATURES')
    with open(PATH + FEATURES, 'rb') as input_file:
        collection_paths, collection_labels, collection_features = pickle.load(input_file)
    collection_dict = {value:index for index,value in enumerate(collection_paths)}
    collection_list = zip(collection_paths, collection_labels)

    pr_results = {}
    roc_results = {}
    for fold_index in range(len(pos_folds)):
        neg_matrix_x = []
        pos_matrix_x = []
        for train_index in range(len(pos_folds)):
            if train_index != fold_index:
                print(' > EXPLORING TRAINING FEATURES - FOLD %d' % (train_index + 1))
                pos_f = pos_folds[train_index]
                neg_f = neg_folds[train_index]
                
                print('  - Positive tuples:')
                for tuple in pos_f: 
                    sample_a, sample_b = mount_tuple(tuple, DATASET)
                    if collection_dict.has_key(sample_a) and collection_dict.has_key(sample_b):
                        feat_a = collection_features[collection_dict[sample_a]]
                        feat_b = collection_features[collection_dict[sample_b]]
                        diff_feat = np.absolute(np.subtract(feat_a, feat_b))
                        pos_matrix_x.append(diff_feat)
                    else:
                        print(sample_a, sample_b, 'NOT FOUND')
                
                print('  - Negative tuples:')
                for tuple in neg_f: 
                    sample_a, sample_b = mount_tuple(tuple, DATASET)
                    if collection_dict.has_key(sample_a) and collection_dict.has_key(sample_b):
                        feat_a = collection_features[collection_dict[sample_a]]
                        feat_b = collection_features[collection_dict[sample_b]]
                        diff_feat = np.absolute(np.subtract(feat_a, feat_b))
                        neg_matrix_x.append(diff_feat)
                    else:
                        print(sample_a, sample_b, 'NOT FOUND')

        print('  - Split into Chunks: %d models, %d samples' % (HASH_MODELS, HASH_SAMPLES))
        neg_splits = []
        pos_splits = []
        assert HASH_SAMPLES < len(neg_matrix_x) and HASH_SAMPLES < len(pos_matrix_x)
        for index in range(HASH_MODELS):
            neg_splits.append(random.sample(neg_matrix_x, HASH_SAMPLES))
            pos_splits.append(random.sample(pos_matrix_x, HASH_SAMPLES))

        print(' > LEARNING PLS MODEL - FOLD %d' % (fold_index + 1))
        models = parallel_pool(
            delayed(learn_plsh_v_model) (pos_s, neg_s) for (pos_s, neg_s) in zip(pos_splits, neg_splits)
        )
        
        results_c = []
        results_v = []
        for test_index in range(len(pos_folds)):
            if test_index == fold_index:
                print(' > EXPLORING TESTING FEATURES - FOLD %d' % (test_index + 1))
                pos_f = pos_folds[test_index]
                neg_f = neg_folds[test_index]
                
                print('  - Positive tuples:')
                for tuple in pos_f: 
                    sample_a, sample_b = mount_tuple(tuple, DATASET)
                    if collection_dict.has_key(sample_a) and collection_dict.has_key(sample_b):
                        feat_a = collection_features[collection_dict[sample_a]]
                        feat_b = collection_features[collection_dict[sample_b]]
                        diff_feat = np.absolute(np.subtract(feat_a, feat_b))
                        response_c = [model.predict_confidence(diff_feat) for model in models]
                        response_v = [model.predict_value(diff_feat) for model in models]
                        results_c.append((np.sum(response_c), 1.0))
                        results_v.append((np.mean(response_v), 1.0))
                        print(sample_a, sample_b, np.sum(response_c), np.mean(response_v))
                    else:
                        print(sample_a, sample_b, 'NOT FOUND')
                
                print('  - Negative tuples:')
                for tuple in neg_f: 
                    sample_a, sample_b = mount_tuple(tuple, DATASET)
                    if collection_dict.has_key(sample_a) and collection_dict.has_key(sample_b):
                        feat_a = collection_features[collection_dict[sample_a]]
                        feat_b = collection_features[collection_dict[sample_b]]
                        diff_feat = np.absolute(np.subtract(feat_a, feat_b))
                        response_c = [model.predict_confidence(diff_feat) for model in models]
                        response_v = [model.predict_value(diff_feat) for model in models]
                        results_c.append((np.sum(response_c), 0.0))
                        results_v.append((np.mean(response_v), 0.0))
                        print(sample_a, sample_b, np.sum(response_c), np.mean(response_v))
                    else:
                        print(sample_a, sample_b, 'NOT FOUND')
        # raw_input('Press ENTER key to continue...')
        plotting_labels = []
        plotting_scores = []
        for res in results_v:
            plotting_labels.append(('_', res[1]))
            plotting_scores.append(('_', res[0]))
            
        pr_results[fold_index] = generate_precision_recall(plotting_labels, plotting_scores)
        roc_results[fold_index] = generate_roc_curve(plotting_labels, plotting_scores)
    return pr_results, roc_results


if __name__ == "__main__":
    main()
    