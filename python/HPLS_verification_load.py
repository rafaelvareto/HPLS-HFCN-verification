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
from auxiliar import learn_plsh_model
from auxiliar import load_txt_file
from auxiliar import split_into_chunks
from joblib import Parallel, delayed
from pls_classifier import PLSClassifier

parser = argparse.ArgumentParser(description='HPLS for Face Recognition with NO Feature Extraction')
parser.add_argument('-p', '--path', help='Path do binary feature file', required=False, default='./features/')
parser.add_argument('-f', '--file', help='Input binary feature file name', required=False, default='PUBFIG-DEV-DEEP-FEATURE-VECTORS.bin')
parser.add_argument('-r', '--rept', help='Number of executions', required=False, default=1)
parser.add_argument('-m', '--hash', help='Number of hash functions', required=False, default=100)
parser.add_argument('-ts', '--train_set_size', help='Default size of training subset', required=False, default=0.5)
args = parser.parse_args()


def main():
    PATH = str(args.path)
    DATASET = str(args.file)
    ITERATIONS = int(args.rept)
    TRAIN_SET_SIZE = float(args.train_set_size)
    NUM_HASH = int(args.hash)
    DATASET = DATASET.replace('-FEATURE-VECTORS.bin','')
    OUTPUT_NAME = 'HPLS_CLOSED_' + DATASET + '_' + str(NUM_HASH) + '_' + str(TRAIN_SET_SIZE) + '_' + str(ITERATIONS)

    cmcs = []
    prs = []
    rocs = []
    with Parallel(n_jobs=-2, verbose=11, backend='multiprocessing') as parallel_pool:
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
    PATH = str(args.path)
    DATASET = str(args.file)
    NUM_HASH = int(args.hash)
    TRAIN_SET_SIZE = float(args.train_set_size)

    print('>> LOADING FEATURES FROM FILE')
    with open(PATH + DATASET, 'rb') as input_file:
        list_of_paths, list_of_labels, list_of_features = pickle.load(input_file)

    matrix_x = []
    matrix_y = []
    plotting_labels = []
    plotting_scores = []
    splits = []
    
    print('>> EXPLORING DATASET')
    individuals = list(set(list_of_labels))
    paths_dict = {value:index for index,value in enumerate(list_of_paths)}
    train_list = zip(list_of_paths, list_of_labels)

    split_into_chunks(train_list)
    raw_input('')

    print('>> LOADING TRAINING TUPLES: {0} samples'.format(len(known_train)))
    counterA = 0
    for train_sample in train_list:
        sample_path = train_sample[0]
        sample_name = train_sample[1]
        sample_index = paths_dict[sample_path]
        feature_vector = list_of_features[sample_index] 
    
        matrix_x.append(feature_vector)
        matrix_y.append(sample_name)

        counterA += 1
        print(counterA, sample_path, sample_name)
    
    print('>> SPLITTING POSITIVE/NEGATIVE SETS: {0} subjects'.format(len(individuals)))
    cmc_score = np.zeros(len(individuals))
    for index in range(0, NUM_HASH):
        splits.append(generate_pos_neg_dict(individuals))

    print('>> LEARNING PLS MODELS:')
    numpy_x = np.array(matrix_x)
    numpy_y = np.array(matrix_y)
    numpy_s = np.array(splits)
    models = parallel_pool(
        delayed(learn_plsh_model) (numpy_x, numpy_y, split) for split in numpy_s
    )
  
    print('>> LOADING KNOWN PROBE: {0} samples'.format(len(known_test)))
    counterB = 0
    for probe_sample in known_test:
        sample_path = probe_sample[0]
        sample_name = probe_sample[1]
        sample_index = paths_dict[sample_path]
        feature_vector = list_of_features[sample_index] 

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
    del list_of_paths[:]
    del list_of_labels[:]
    del list_of_features[:]
    
    cmc = np.divide(cmc_score, counterB) 
    pr = generate_precision_recall(plotting_labels, plotting_scores)
    roc = generate_roc_curve(plotting_labels, plotting_scores)
    return cmc, pr, roc

if __name__ == "__main__":
    main()
    