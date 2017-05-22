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
from auxiliar import plot_cmc_curve
from auxiliar import learn_plsh_model, learn_plsh_v_model
from auxiliar import load_txt_file, read_fold_file
from auxiliar import split_into_chunks
from joblib import Parallel, delayed
from pls_classifier import PLSClassifier

parser = argparse.ArgumentParser(description='HPLS for Face Verification with NO Feature Extraction')
parser.add_argument('-p', '--path', help='Path do binary feature file', required=False, default='./features/')
parser.add_argument('-c', '--collection', help='Input file name containing folds', required=False, default='./datasets/pubfig/pubfig_full.txt')
parser.add_argument('-fts', '--features_test', help='Input containing binary FEATURES_TRAIN', required=False, default='PUBFIG-EVAL-DEEP.bin')
parser.add_argument('-ftr', '--features_train', help='Input containing binary FEATURES_TRAIN', required=False, default='PUBFIG-DEV-DEEP.bin')
parser.add_argument('-fo', '--fold', help='Fold number used to test', required=False, default=None)
parser.add_argument('-hm', '--hash_models', help='Number of hash functions', required=False, default=100)
parser.add_argument('-it', '--iterations', help='Number of executions', required=False, default=1)
args = parser.parse_args()

PATH = str(args.path)
COLLECTION = str(args.collection)
FEATURES_TEST = str(args.features_test)
FEATURES_TRAIN = str(args.features_train)
FOLD = str(args.fold)
HASH_MODELS = int(args.hash_models)
ITERATIONS = int(args.iterations)
OUTPUT_NAME = 'HPLS_CROSS_VER_' + FEATURES_TRAIN + '_' + FEATURES_TEST + '_' + str(FOLD) + '_' + str(HASH_MODELS) + '_' + str(ITERATIONS)


def main():
    prs = []
    rocs = []
    with Parallel(n_jobs=1, verbose=11, backend='multiprocessing') as parallel_pool:
        for index in range(ITERATIONS):
            print('ITERATION #%s' % str(index+1))
            pr, roc = hplsfacev(args, parallel_pool)
            prs.append(pr)
            rocs.append(roc)

            with open('./files/' + OUTPUT_NAME + '.file', 'w') as outfile:
                pickle.dump([prs, rocs], outfile)

            plot_precision_recall(prs, OUTPUT_NAME)
            plot_roc_curve(rocs, OUTPUT_NAME)


def hplsfacev(args, parallel_pool):
    print('>> LOADING TRAINING FEATURES')
    with open(PATH + FEATURES_TRAIN, 'rb') as input_file:
        train_paths, train_labels, train_features = pickle.load(input_file)
    
    print('>> EXPLORING TRAINING FEATURES')
    train_dict = {value:index for index,value in enumerate(train_paths)}
    train_list = zip(train_paths, train_labels)
    pos_splits, neg_splits = split_into_chunks(train_list, HASH_MODELS)

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
    assert len(pos_folds) == len(neg_folds)
    with open(PATH + FEATURES_TEST, 'rb') as input_file:
        test_paths, test_labels, test_features = pickle.load(input_file)

    print('>> EXPLORING PROBE FEATURES')
    test_dict = {value:index for index,value in enumerate(test_paths)}
    test_list = zip(test_paths, test_labels)

    fold_results = []
    # for (pos_f, neg_f) in zip(pos_folds, neg_folds):
    pos_f = pos_folds[0]
    neg_f = neg_folds[0]
        
    results_c = []
    results_v = []
    
    print('> Positive probes:')
    for pos in pos_f:
        sample_a = pos[0] + '/' + pos[1] + '.jpg'
        sample_b = pos[2] + '/' + pos[3] + '.jpg'
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
    for neg in neg_f:
        sample_a = neg[0] + '/' + neg[1] + '.jpg'
        sample_b = neg[2] + '/' + neg[3] + '.jpg'
        if test_dict.has_key(sample_a) and test_dict.has_key(sample_b):
            feat_a = test_features[test_dict[sample_a]]
            feat_b = test_features[test_dict[sample_b]]
            diff_feat = np.absolute(np.subtract(feat_a, feat_b))
            response_c = [model[0].predict_confidence(diff_feat) for model in models]
            response_v = [model[0].predict_value(diff_feat) for model in models]
            results_c.append((np.sum(response_c), 0))
            results_v.append((np.mean(response_v), 0))
            print(sample_a, sample_b, np.sum(response_c), np.mean(response_v))
    
    del models[:]
    plotting_labels = []
    plotting_scores = []
    for res in results_c:
        plotting_labels.append(('_', res[1]))
        plotting_scores.append(('_', res[0]))

    pr = generate_precision_recall(plotting_labels, plotting_scores)
    roc = generate_roc_curve(plotting_labels, plotting_scores)
    return pr, roc


if __name__ == "__main__":
    main()
    