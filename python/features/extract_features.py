import os
# os.environ["THEANO_FLAGS"] = "device=gpu0"

import argparse
import cv2 as cv
import numpy as np
import pickle
import sys

sys.path.append('../')
from descriptor import Descriptor

parser = argparse.ArgumentParser(description='Feature Extraction')
parser.add_argument('-p', '--path', help='Path do dataset', required=False, default='/Users/vareto/Downloads/PubFig/dev_cropped/')
parser.add_argument('-f', '--file', help='Input file name', required=False, default='dev_set.txt')
parser.add_argument('-d', '--desc', help='Descriptor [hog/df]', required=False, default='df')
parser.add_argument('-iw', '--width', help='Default image width', required=False, default=128)
parser.add_argument('-ih', '--height', help='Default image height', required=False, default=144)
args = parser.parse_args()


def main():
    PATH = str(args.path)
    DATASET = str(args.file)
    DESCRIPTOR = str(args.desc)
    OUTPUT_NAME = 'features_' + DESCRIPTOR + '_' + DATASET.replace('.txt','.bin')

    print('EXTRACTING FEATURES')
    dataset_list = load_txt_file(PATH + DATASET)
    feat_z, feat_y, feat_x = extract_features(args, dataset_list)
    
    print('SAVING TO FILE')
    outmatrix = [feat_z, feat_y, feat_x]
    with open(OUTPUT_NAME, 'wb') as outfile:
        pickle.dump(outmatrix, outfile, protocol=pickle.HIGHEST_PROTOCOL)


def load_txt_file(file_name):
    this_file = open(file_name, 'r')
    this_list = []
    for line in this_file:
        line = line.rstrip()
        components = line.split()
        this_list.append(components)
    return this_list


def extract_features(arguments, dataset_list):
    PATH = str(arguments.path)
    DATASET = str(arguments.file)
    DESCRIPTOR = str(arguments.desc)
    IMG_WIDTH = int(arguments.width)
    IMG_HEIGHT = int(arguments.height)

    matrix_x = []
    matrix_y = []
    matrix_z = []

    vgg_model = None
    if DESCRIPTOR == 'df':
        from vggface import VGGFace
        vgg_model = VGGFace()

    counterA = 0
    for sample in dataset_list:
        try:
            sample_path = sample[0]
            sample_name = sample[1]
            subject_path = PATH + sample_path
            subject_image = cv.imread(subject_path, cv.IMREAD_COLOR)

            if DESCRIPTOR == 'hog':
                subject_image = cv.resize(subject_image, (IMG_HEIGHT, IMG_WIDTH))
                feature_vector = Descriptor.get_hog(subject_image)
            elif DESCRIPTOR == 'df':
                feature_vector = Descriptor.get_deep_feature(subject_image, vgg_model, layer_name='fc6')

            matrix_x.append(feature_vector)
            matrix_y.append(sample_name)
            matrix_z.append(sample_path)
            
            print(counterA, sample_path, sample_name, len(feature_vector))

        except Exception, e:
            print(counterA, sample_path + ' not loaded', str(e))
        counterA += 1

    return matrix_z, matrix_y, matrix_x


if __name__ == "__main__":
    main()