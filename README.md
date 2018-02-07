# HSVM-HPLS-verification
Face recognition has been one of the most important tasks in computer vision due to the wide range of applications in several environments, such as surveillance systems, biometrics, forensics. 
One of the face recognition tasks, the face verification is responsible for  determining whether two facial images belong to the same subject (i.e., genuine matching) or are from different subjects (i.e., an impostor). 
An example of face verification is the following. 
Imagine you are at a bank ATM machine, the system will take your picture, extract its features and match them to your biometric information (template) stored in the bank database based on the account number you entered. 
If there is a positive match, you will have access granted to your account.

## Approach
We based the proposed framework on two hypotheses:
* Two face images of the same subject would hold small differences, but this difference increases when we consider a pair of images from different subjects; 
* Multiple classifiers might achieve higher verification rates due to higher diversity.

Two sets of disparity feature vectors (same and not same) are used to learn each of k Partial Least Squares (PLS) model. To increase the diversity, each PLS model is estimated using sets with different samples. Then, the disparity features are extracted from a pair of testing images to compose a feature vector which is classified by each PLS model, from which the response values are used to estimate the label (genuine or impostor), based on a majority voting scheme

### Reference Paper
This framework was developed during the pursuance of my Master's degree in collaboration with Samira Silva, Filipe Costa and Professor William Schwartz.
If you find this work interesting, please cite our work:
```
@conference
{ vareto2017verification,
  title={Face Verification based on Relational Disparity Features and Partial Least Squares Models},
  author={Vareto, Rafael and Silva, Samira and Costa, Filipe and Schwartz, William Robson},
  booktitle={2017 30th IEEE International Conference on Graphics, Patterns and Images (SIBGRAPI)},
  pages={209--215},
  year={2017},
  organization={IEEE}
}
```
*Rafael Vareto, Samira Silva, Filipe Costa, William Robson Schwartz. Face Verification based on Relational Disparity Features and Partial Least Squares Models. IEEE International Conference on Graphics, Patterns and Images (SIBGRAPI), 2017.* [[PDF](http://www.dcc.ufmg.br/~william/papers/paper_2017_SIBGRAPI_Vareto.pdf)]


## Getting Started
The instructions below will get you a copy of the project up and running on your local machine for development and testing purposes. If you have any doubts about implementation and deployment, do not hesitate contating me at my [PERSONAL HOMEPAGE](http://homepages.dcc.ufmg.br/~rafaelvareto/).
To clone this repository, simply enter the following command in your terminal:
```bash
git clone https://github.com/rafaelvareto/HPLS-verification.git
```

### Installation Process

The method described herein was desgined and evaluated on a linux-based machine with [Python 2.7.6](https://www.python.org/) and [OpenCV 3.1.0](https://github.com/Itseez/opencv.git).
In addition to OpenCV, the following Python libraries are required in order to execute our full pipeline: H5PY, JOBLIB, MATPLOTLIB, NUMPY, PILLOW, SCIKIT, SCIPY, TENSORFLOW, THEANO and KERAS to name a few.

First of all, you should make sure that a recent version of OpenCV is installed in your system.
We recommend installing the default OpenCV and its additional modules (contrib).
For a complete installation guide, please check this [link](https://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/) out.
If you think no contrib module is indeed necessary, you can install OpenCV according to the following terminal commands (Linux):

Essential compiling libraries:
```bash
sudo apt-get install build-essential checkinstall cmake pkg-config yasm
```

Handling different image formats:
```bash
sudo apt-get install libtiff5-dev libpng16-dev libjpeg8-dev libjasper-dev
```

Handling different video formats:
```bash
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev
```

Python development libraries:
```bash
sudo apt-get install python-dev libpython-all-dev libtbb-dev
```

Now you can clone OpenCV repository before installing it on your system:
```bash
cd ~
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.1.0
```

Time to setup the build:
```bash
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_TBB=ON \
    -D WITH_FFMPEG=ON \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D BUILD_EXAMPLES=ON ..
```

In addition to OpenCV, the following Python libraries are required in order to execute our full pipeline:
```bash
* pip install cerberus
* pip install h5py
* pip install joblib
* pip install matplotlib
* pip install numpy
* pip install pillow
* pip install scikit-learn
* pip install scipy
* pip install sympy

* pip install tensorflow
* pip install theano
* pip install keras
```


### Datasets
In order to reproduce the experiments, you need to either download the utilized datasets (LFW and PubFig) and extract their corresponding feature vectors or download their disclosed feature files:
* Labeled Faces in the Wild [[vgg](http://homepages.dcc.ufmg.br/~rafaelvareto/features/LFW-DEEP.bin)]
* Public Figures [[vgg-dev](http://homepages.dcc.ufmg.br/~rafaelvareto/features/PUBFIG-DEV-DEEP.bin)] [[vgg-eval](http://homepages.dcc.ufmg.br/~rafaelvareto/features/PUBFIG-EVAL-DEEP.bin)]

Note that PubFig was released long ago and they do not distribute image files due to copyright issues. Thus, only 26.787 out of 58.797 initially images remain available as links to these files are gradually disappearing over time.


### Deployment Process
The python folder contains all the code employed in the experiments detailed in our [SIBGRAPI conference paper](http://www.dcc.ufmg.br/~william/papers/paper_2017_SIBGRAPI_Vareto.pdf).
There are many python codes, however the main files are:
* **HPLS_verification_load.py:** This file runs an embedding of classifiers comprised of binary partial least squares models.
* **HSVM_verification_load.py:** This file runs an embedding of classifiers comprised of binary support vector machine models.

**FYI:** The main difference between *load* and *feat* files is that the former is configure to load dataset feature vectors from files (links are available above) whereas the latter extracts features at execution time.

Folder *bash* contains a series of bash scripts for PLS and SVM.
Besides, it is also composed of two subfolders: *files* and *plots*. Make sure these two folders exist so that the algorithms can save ouput files and plots for validation.

Folder *datasets* is supposed to keep the datasets images.
Remember that when datasets image samples are explored, you must use *feat* python files or extract features using *features/extract_features.py* to use *load* python files.

Folder *features* is supposed to keep the datasets extracted feature files.
Remember that when datasets image samples are explored, you must use *load* python files.
In order to open feature files, use the following python command:
```python
import pickle
file_name = 'FRGC-SET-4-DEEP.bin'
with open(file_name, 'rb') as infile:
    matrix_z, matrix_y, matrix_x = pickle.load(infile)
```

Suppose you have installed all the necessary Python requirements and downloaded all necessary *.bin*-feature dataset files.
Assuming that you are on this repository's *python* folder and the feature files are stored in the *python/features*, you can run the developed methods by simply typing the following command in terminal:
```bash
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 005 -hs 50 -it 10
```
Where **-p** determines the feature path, **-c** is the text file specifying folds, **-d** indicates the dataset name, **-f** specifies the feature file, **-hm** defines the number of binary models, **-hs** specifies the number of samples per hash model, and **-it** indicates the number of repetitions.
