#!/bin/bash

#HOG
echo 'LFW: HOG, Variable hashing, 10% Train'
python ../HPLS_closedset_load.py -p ../features/ -f LFW-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f LFW-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f LFW-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.1

echo 'LFW: HOG, Variable hashing, 50% Train'
python ../HPLS_closedset_load.py -p ../features/ -f LFW-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f LFW-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f LFW-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'LFW: HOG, Variable hashing, 90% Train'
python ../HPLS_closedset_load.py -p ../features/ -f LFW-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f LFW-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f LFW-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.9

#DF
echo 'LFW: DF, Variable hashing, 10% Train'
python ../HPLS_closedset_load.py -p ../features/ -f LFW-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f LFW-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f LFW-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.1

echo 'LFW: DF, Variable hashing, 50% Train'
python ../HPLS_closedset_load.py -p ../features/ -f LFW-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f LFW-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f LFW-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'LFW: DF, Variable hashing, 90% Train'
python ../HPLS_closedset_load.py -p ../features/ -f LFW-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f LFW-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f LFW-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.9