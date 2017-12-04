import argparse
import cv2 as cv
import itertools
import matplotlib
import numpy as np
import pickle
import time

matplotlib.use('Agg')

from auxiliar import generate_pos_neg_dict
from auxiliar import generate_precision_recall, plot_precision_recall
from auxiliar import generate_roc_curve, plot_roc_curve
from auxiliar import iteration_to_fold
from auxiliar import learn_svmh_cv_model
from auxiliar import load_txt_file, read_fold_file
from auxiliar import mount_tuple
from auxiliar import split_into_chunks
from joblib import Parallel, delayed

parser = argparse.ArgumentParser(description='HSVM for cross-dataset Face Verification with NO Feature Extraction')
parser.add_argument('-p', '--path', help='Path do binary feature file', required=False, default='./features/')
parser.add_argument('-c', '--collection', help='Input file name containing folds', required=False, default='./datasets/pubfig/pubfig_full.txt')
parser.add_argument('-d', '--dataset', help='Dataset name', required=False, default='lfw')
parser.add_argument('-ftr', '--features_train', help='Input containing binary FEATURES_TRAIN', required=False, default='PUBFIG-DEV-DEEP.bin')
parser.add_argument('-fts', '--features_test', help='Input containing binary FEATURES_TEST', required=False, default='PUBFIG-EVAL-DEEP.bin')
parser.add_argument('-hm', '--hash_models', help='Number of hash functions', required=False, default=100)
parser.add_argument('-hs', '--hash_samples', help='Number of samples per hash model', required=False, default=100)
parser.add_argument('-it', '--iterations', help='Number of executions', required=False, default=1)
args = parser.parse_args()

PATH = str(args.path)
COLLECTION = str(args.collection)
FEATURES_TEST = str(args.features_test)
FEATURES_TRAIN = str(args.features_train)
DATASET = str(args.dataset)
HASH_MODELS = int(args.hash_models)
HASH_SAMPLES = int(args.hash_samples)
ITERATIONS = int(args.iterations)
TRAIN_SET = FEATURES_TRAIN.replace('-DEEP.bin', '')
TEST_SET = FEATURES_TEST.replace('-DEEP.bin', '')
OUTPUT_NAME = 'HSVM_CROS_' + TRAIN_SET + '_' + TEST_SET + '_' + str(args.hash_models) + '_' + str(args.hash_samples) + '_' + str(args.iterations)


def main():
    prs = []
    rocs = []
    times = []
    with Parallel(n_jobs=4, verbose=11, backend='multiprocessing') as parallel_pool:
        for index in range(ITERATIONS):
            print('ITERATION #%s' % str(index+1))
            start_time = time.time()
            pr, roc = hsvmfacev(args, parallel_pool)
            end_time = time.time()
            
            abs_time = (end_time - start_time) / 10
            prs.append(pr)
            rocs.append(roc)
            times.append(abs_time)
            
            prs_f, rocs_f = iteration_to_fold(prs, rocs)
            with open('./files/' + OUTPUT_NAME + '.file', 'w') as outfile:
                pickle.dump([prs_f, rocs_f], outfile)
            for index in range(len(prs_f)):
                plot_precision_recall(prs_f[index], OUTPUT_NAME + '_fold_' + str(index + 1))
            for index in range(len(rocs_f)):
                plot_roc_curve(rocs_f[index], OUTPUT_NAME + '_fold_' + str(index + 1))
            with open('./times/' + OUTPUT_NAME + '.time', 'a') as outtime:
                outtime.write(str(abs_time) + '\n')
        with open('./times/' + OUTPUT_NAME + '.time', 'a') as outtime:
            outtime.write('------\n')
            outtime.write(str(np.mean(times)) + '\n')
            outtime.write(str(np.std(times)) + '\n')


def hsvmfacev(args, parallel_pool):
    print('>> LOADING TRAINING FEATURES')
    with open(PATH + FEATURES_TRAIN, 'rb') as input_file:
        train_paths, train_labels, train_features = pickle.load(input_file)
    
    print('>> EXPLORING TRAINING FEATURES')
    train_dict = {value:index for index,value in enumerate(train_paths)}
    train_list = zip(train_paths, train_labels)
    pos_splits, neg_splits = split_into_chunks(train_list, HASH_MODELS, HASH_SAMPLES)

    print('>> LEARNING SVM MODELS:')
    models = parallel_pool(
        delayed(learn_svmh_cv_model) (train_features, train_dict, pos_s, neg_s) for (pos_s, neg_s) in zip(pos_splits, neg_splits)
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
            
        results = []
        print('> Positive probes:')
        for tuple in pos_f:
            sample_a, sample_b = mount_tuple(tuple, DATASET)
            if test_dict.has_key(sample_a) and test_dict.has_key(sample_b):
                feat_a = test_features[test_dict[sample_a]]
                feat_b = test_features[test_dict[sample_b]]
                diff_feat = np.absolute(np.subtract(feat_a, feat_b))
                response = [model[0].predict([diff_feat]) for model in models]
                results.append((np.sum(response), 1.0))
                print(sample_a, sample_b, np.sum(response))
        
        print('> Negative probes:')
        for tuple in neg_f:
            sample_a, sample_b = mount_tuple(tuple, DATASET)
            if test_dict.has_key(sample_a) and test_dict.has_key(sample_b):
                feat_a = test_features[test_dict[sample_a]]
                feat_b = test_features[test_dict[sample_b]]
                diff_feat = np.absolute(np.subtract(feat_a, feat_b))
                response = [model[0].predict([diff_feat]) for model in models]
                results.append((np.sum(response), 0.0))
                print(sample_a, sample_b, np.sum(response))
                
        plotting_labels = []
        plotting_scores = []
        for res in results:
            plotting_labels.append(('_', res[1]))
            plotting_scores.append(('_', res[0]))
            
        pr_results[fold_index] = generate_precision_recall(plotting_labels, plotting_scores)
        roc_results[fold_index] = generate_roc_curve(plotting_labels, plotting_scores)
    del models[:]
    return pr_results, roc_results


if __name__ == "__main__":
    main()
    