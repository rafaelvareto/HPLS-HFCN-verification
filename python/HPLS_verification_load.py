import argparse
import cv2 as cv
import itertools
import matplotlib
import numpy as np
import pickle

matplotlib.use('Agg')

from auxiliar import generate_pos_neg_dict
from auxiliar import generate_precision_recall, plot_precision_recall
from auxiliar import generate_roc_curve, plot_roc_curve
from auxiliar import iteration_to_fold
from auxiliar import learn_plsh_model, learn_plsh_v_model
from auxiliar import load_txt_file, read_fold_file
from auxiliar import split_into_chunks
from joblib import Parallel, delayed
from pls_classifier import PLSClassifier

parser = argparse.ArgumentParser(description='HPLS for Face Verification with NO Feature Extraction')
parser.add_argument('-p', '--path', help='Path do binary feature file', required=False, default='./features/')
parser.add_argument('-c', '--collection', help='Input file name containing folds', required=False, default='./datasets/lfw/lfw_pairs.txt')
parser.add_argument('-fts', '--features_test', help='Input containing binary FEATURES_TRAIN', required=False, default='LFW-DEEP.bin')
parser.add_argument('-ftr', '--features_train', help='Input containing binary FEATURES_TRAIN', required=False, default='PUBFIG-DEV-DEEP.bin')
parser.add_argument('-hm', '--hash_models', help='Number of hash functions', required=False, default=100)
parser.add_argument('-hs', '--hash_samples', help='Number of samples per hash model', required=False, default=100)
parser.add_argument('-it', '--iterations', help='Number of executions', required=False, default=2)
args = parser.parse_args()

PATH = str(args.path)
COLLECTION = str(args.collection)
FEATURES_TEST = str(args.features_test)
FEATURES_TRAIN = str(args.features_train)
HASH_MODELS = int(args.hash_models)
HASH_SAMPLES = int(args.hash_samples)
ITERATIONS = int(args.iterations)
TRAIN_SET = FEATURES_TRAIN.replace('-DEEP.bin', '')
TEST_SET = FEATURES_TEST.replace('-DEEP.bin', '')
OUTPUT_NAME = 'HPLS_V_' + TRAIN_SET + '_' + TEST_SET + '_' + str(HASH_MODELS) + '_' + str(HASH_SAMPLES) + '_' + str(ITERATIONS)


def main():
    prs = []
    rocs = []
    with Parallel(n_jobs=1, verbose=11, backend='multiprocessing') as parallel_pool:
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
    print('>> LOADING TRAINING FEATURES')
    with open(PATH + FEATURES_TRAIN, 'rb') as input_file:
        train_paths, train_labels, train_features = pickle.load(input_file)
    
    print('>> EXPLORING TRAINING FEATURES')
    train_dict = {value:index for index,value in enumerate(train_paths)}
    train_list = zip(train_paths, train_labels)
    pos_splits, neg_splits = split_into_chunks(train_list, HASH_MODELS, HASH_SAMPLES)

    print('>> LEARNING PLS MODELS:')
    models = parallel_pool(
        delayed(learn_plsh_v_model) (train_features, train_dict, pos_s, neg_s) for (pos_s, neg_s) in zip(pos_splits, neg_splits)
    )

    print('>> REMOVING TRAINING FEATURES')
    del train_paths[:]
    del train_labels[:]
    del train_features[:]

    print('>> LOADING PROBE FEATURES')
    pos_folds, neg_folds = read_fold_file(COLLECTION)
    with open(PATH + FEATURES_TEST, 'rb') as input_file:
        test_paths, test_labels, test_features = pickle.load(input_file)

    print('>> EXPLORING PROBE FEATURES')
    test_dict = {value:index for index,value in enumerate(test_paths)}
    test_list = zip(test_paths, test_labels)

    assert len(pos_folds) == len(neg_folds)
    pr_results = {}
    roc_results = {}
    for fold_index in range(len(pos_folds)):
        print('>> Fold #%s' % str(fold_index + 1))
        pos_f = pos_folds[fold_index]
        neg_f = neg_folds[fold_index]
            
        results_c = []
        results_v = []
        
        print('> Positive probes:')
        for probe in pos_f:
            sample_a = probe[0] + '/' + probe[0] + '_' + format(int(probe[1]),'04d') + '.jpg'
            sample_b = probe[2] + '/' + probe[2] + '_' + format(int(probe[3]),'04d') + '.jpg'
            if test_dict.has_key(sample_a) and test_dict.has_key(sample_b):
                feat_a = test_features[test_dict[sample_a]]
                feat_b = test_features[test_dict[sample_b]]
                diff_feat = np.absolute(np.subtract(feat_a, feat_b))
                response_c = [model[0].predict_confidence(diff_feat) for model in models]
                response_v = [model[0].predict_value(diff_feat) for model in models]
                results_c.append((np.sum(response_c), 1))
                results_v.append((np.mean(response_v), 1))
                print(sample_a, sample_b, np.sum(response_c), np.mean(response_v))
        
        print('> Negative probes:')
        for probe in neg_f:
            sample_a = probe[0] + '/' + probe[0] + '_' + format(int(probe[1]),'04d') + '.jpg'
            sample_b = probe[2] + '/' + probe[2] + '_' + format(int(probe[3]),'04d') + '.jpg'
            if test_dict.has_key(sample_a) and test_dict.has_key(sample_b):
                feat_a = test_features[test_dict[sample_a]]
                feat_b = test_features[test_dict[sample_b]]
                diff_feat = np.absolute(np.subtract(feat_a, feat_b))
                response_c = [model[0].predict_confidence(diff_feat) for model in models]
                response_v = [model[0].predict_value(diff_feat) for model in models]
                results_c.append((np.sum(response_c), 0))
                results_v.append((np.mean(response_v), 0))
                print(sample_a, sample_b, np.sum(response_c), np.mean(response_v))
                
        plotting_labels = []
        plotting_scores = []
        for res in results_v:
            plotting_labels.append(('_', res[1]))
            plotting_scores.append(('_', res[0]))
            
        pr_results[fold_index] = generate_precision_recall(plotting_labels, plotting_scores)
        roc_results[fold_index] = generate_roc_curve(plotting_labels, plotting_scores)
    del models[:]
    return pr_results, roc_results


if __name__ == "__main__":
    main()
    