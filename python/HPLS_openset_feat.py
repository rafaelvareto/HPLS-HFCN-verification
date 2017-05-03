import argparse
import cv2 as cv
import itertools
import matplotlib
import numpy as np
import pickle

matplotlib.use('Agg')

from auxiliar import generate_cmc_curve
from auxiliar import generate_pos_neg_dict
from auxiliar import generate_precision_recall, plot_precision_recall
from auxiliar import generate_roc_curve, plot_roc_curve
from auxiliar import learn_plsh_model
from auxiliar import load_txt_file
from auxiliar import split_known_unknown_sets, split_train_test_sets
from descriptor import Descriptor
from joblib import Parallel, delayed
from matplotlib import pyplot
from pls_classifier import PLSClassifier


parser = argparse.ArgumentParser(description='HPLS for Face Recognition with Feature Extraction')
parser.add_argument('-p', '--path', help='Path do dataset', required=False, default='./frgcv1/')
parser.add_argument('-f', '--file', help='Input file name', required=False, default='train_2_small.txt')
parser.add_argument('-d', '--desc', help='Descriptor [hog/df]', required=False, default='hog')
parser.add_argument('-r', '--rept', help='Number of executions', required=False, default=1)
parser.add_argument('-m', '--hash', help='Number of hash functions', required=False, default=100)
parser.add_argument('-iw', '--width', help='Default image width', required=False, default=128)
parser.add_argument('-ih', '--height', help='Default image height', required=False, default=144)
parser.add_argument('-ks', '--known_set_size', help='Default size of enrolled subjects', required=False, default=0.5)
parser.add_argument('-ts', '--train_set_size', help='Default size of training subset', required=False, default=0.5)
args = parser.parse_args()


def main():
    PATH = str(args.path)
    DATASET = str(args.file)
    DESCRIPTOR = str(args.desc)
    ITERATIONS = int(args.rept)
    KNOWN_SET_SIZE = float(args.known_set_size)
    TRAIN_SET_SIZE = float(args.train_set_size)
    NUM_HASH = int(args.hash)
    
    DATASET = DATASET.replace('.txt','')
    OUTPUT_NAME = 'HPLS_' + DATASET + '_' + DESCRIPTOR + '_' + str(NUM_HASH) + '_' + str(KNOWN_SET_SIZE) + '_' + str(TRAIN_SET_SIZE) + '_' + str(ITERATIONS)

    prs = []
    rocs = []
    with Parallel(n_jobs=-2, verbose=11, backend='multiprocessing') as parallel_pool:
        for index in range(ITERATIONS):
            print('ITERATION #%s' % str(index+1))
            pr, roc = hplsface(args, parallel_pool)
            prs.append(pr)
            rocs.append(roc)

            with open('../files/' + OUTPUT_NAME + '.file', 'w') as outfile:
                pickle.dump([prs, rocs], outfile)

            plot_precision_recall(prs, OUTPUT_NAME)
            plot_roc_curve(rocs, OUTPUT_NAME)


def hplsface(args, parallel_pool):
    PATH = str(args.path)
    DATASET = str(args.file)
    DESCRIPTOR = str(args.desc)
    NUM_HASH = int(args.hash)
    IMG_WIDTH = int(args.width)
    IMG_HEIGHT = int(args.height)
    KNOWN_SET_SIZE = float(args.known_set_size)
    TRAIN_SET_SIZE = float(args.train_set_size)

    matrix_x = []
    matrix_y = []
    splits = []

    plotting_labels = []
    plotting_scores = []

    vgg_model = None
    if DESCRIPTOR == 'df':
        from vggface import VGGFace
        vgg_model = VGGFace()
    
    print('>> EXPLORING DATASET')
    dataset_list = load_txt_file(PATH + DATASET)
    known_tuples, unknown_tuples = split_known_unknown_sets(dataset_list, known_set_size=KNOWN_SET_SIZE)
    known_train, known_test = split_train_test_sets(known_tuples, train_set_size=TRAIN_SET_SIZE)

    print('>> LOADING GALLERY: {0} samples'.format(len(known_train)))
    counterA = 0
    for gallery_sample in known_train:
        sample_path = gallery_sample[0]
        sample_name = gallery_sample[1]

        counterA += 1
        print(counterA, sample_path, sample_name)
        
        gallery_path = PATH + sample_path
        gallery_image = cv.imread(gallery_path, cv.IMREAD_COLOR)
        
        if DESCRIPTOR == 'hog':
            gallery_image = cv.resize(gallery_image, (IMG_HEIGHT, IMG_WIDTH))
            feature_vector = Descriptor.get_hog(gallery_image)
        elif DESCRIPTOR == 'df':
            feature_vector = Descriptor.get_deep_feature(gallery_image, vgg_model, layer_name='fc6')
        del gallery_image
    
        matrix_x.append(feature_vector)
        matrix_y.append(sample_name)
    
    print('>> SPLITTING POSITIVE/NEGATIVE SETS')
    individuals = list(set(matrix_y))
    cmc_score = np.zeros(len(individuals))
    for index in range(0, NUM_HASH):
        splits.append(generate_pos_neg_dict(individuals))

    print('>> LEARNING PLS MODELS:')
    input_list = itertools.izip(splits, itertools.repeat((matrix_x, matrix_y)))
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

        query_path = PATH + sample_path
        query_image = cv.imread(query_path, cv.IMREAD_COLOR)
        if DESCRIPTOR == 'hog':
            query_image = cv.resize(query_image, (IMG_HEIGHT, IMG_WIDTH))
            feature_vector = Descriptor.get_hog(query_image)
        elif DESCRIPTOR == 'df':
            feature_vector = Descriptor.get_deep_feature(query_image, vgg_model)

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

    print('>> LOADING UNKNOWN PROBE: {0} samples'.format(len(unknown_tuples)))
    counterC = 0
    for probe_sample in unknown_tuples:
        sample_path = probe_sample[0]
        sample_name = probe_sample[1]

        query_path = PATH + sample_path 
        query_image = cv.imread(query_path, cv.IMREAD_COLOR)
        if DESCRIPTOR == 'hog':
            query_image = cv.resize(query_image, (IMG_HEIGHT, IMG_WIDTH))
            feature_vector = Descriptor.get_hog(query_image)
        elif DESCRIPTOR == 'df':    
            feature_vector = Descriptor.get_deep_feature(query_image, vgg_model)

        vote_dict = dict(map(lambda vote: (vote, 0), individuals))
        for model in models:
            pos_list = [key for key, value in model[1].iteritems() if value == 1]
            response = model[0].predict_confidence(feature_vector)
            for pos in pos_list:
                vote_dict[pos] += response
        result = vote_dict.items()
        result.sort(key=lambda tup: tup[1], reverse=True)

        counterC += 1
        denominator = np.absolute(np.mean([result[1][1], result[2][1]]))
        if denominator > 0:
            output = result[0][1] / denominator
        else:
            output = result[0][1]
        print(counterC, sample_name, result[0][0], output)

        # Getting unknown set plotting relevant information
        plotting_labels.append([(sample_name, -1)])
        plotting_scores.append([(sample_name, output)])

    # cmc_score_norm = np.divide(cmc_score, counterA)
    # generate_cmc_curve(cmc_score_norm, DATASET + '_' + str(NUM_HASH) + '_' + DESCRIPTOR)
    
    pr = generate_precision_recall(plotting_labels, plotting_scores)
    roc = generate_roc_curve(plotting_labels, plotting_scores)
    return pr, roc

if __name__ == "__main__":
    main()
