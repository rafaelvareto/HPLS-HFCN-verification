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
    cmcs = []
    prs = []
    rocs = []
    with Parallel(n_jobs=1, verbose=11, backend='multiprocessing') as parallel_pool:
        for index in range(ITERATIONS):
            print('ITERATION #%s' % str(index+1))
            cmc, pr, roc = hplsfacev(args, parallel_pool)
            cmcs.append(cmc)
            prs.append(pr)
            rocs.append(roc)

            with open('./files/' + OUTPUT_NAME + '.file', 'w') as outfile:
                pickle.dump([cmcs, prs, rocs], outfile)

            # plot_cmc_curve(cmcs, OUTPUT_NAME)
            plot_precision_recall(prs, OUTPUT_NAME)
            plot_roc_curve(rocs, OUTPUT_NAME)


def hplsfacev(args, parallel_pool):
    plotting_labels = []
    plotting_scores = []

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

    fold_results = dict()
    for (pos, neg) in zip(pos_folds, neg_folds):
        print(pos[0], neg[0])


    print('>> LOADING KNOWN PROBE: {0} samples'.format(len(known_test)))
    counterB = 0
    for probe_sample in known_test:
        sample_path = probe_sample[0]
        sample_name = probe_sample[1]
        sample_index = train_dict[sample_path]
        feature_vector = train_FEATURES_TRAIN[sample_index] 

        if len(feature_vector) > 1:
            vote_dict = dict(map(lambda vote: (vote, 0), individuals))
            for model in models:
                pos_list = [key for key, value in model[1].iteritems() if value == 1]
                response = model[0].predict_confidence(feature_vector)
                for pos in pos_list:
                    vote_dict[pos] += response
            result = vote_dict.items()
            result.sort(key=lambda tup: tup[1], reverse=True)

            for outer in range(len(individuals)):
                for inner in range(outer + 1):
                    if result[inner][0] == sample_name:
                        cmc_score[outer] += 1
                        break
            
            counterB += 1
            denominator = np.absolute(np.mean([result[1][1], result[2][1]]))
            if denominator > 0:
                output = result[0][1] / denominator
            else:
                output = result[0][1]
            print(counterB, sample_name, result[0][0], output)

            # Getting known set plotting relevant information
            plotting_labels.append([(sample_name, 1)])
            plotting_scores.append([(sample_name, output)])
        else:
            print('EMPTY FEATURE VECTOR')

    del models[:]
    
    cmc = np.divide(cmc_score, counterB) 
    pr = generate_precision_recall(plotting_labels, plotting_scores)
    roc = generate_roc_curve(plotting_labels, plotting_scores)
    return cmc, pr, roc


if __name__ == "__main__":
    main()
    