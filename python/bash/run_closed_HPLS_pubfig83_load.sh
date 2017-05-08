#!/bin/bash

#HOG
echo 'PUPFIG83: HOG, Variable hashing, 10% Train'
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.1

echo 'PUPFIG83: HOG, Variable hashing, 50% Train'
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'PUPFIG83: HOG, Variable hashing, 90% Train'
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.9

#DF
echo 'PUPFIG83: DF, Variable hashing, 10% Train'
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.1

echo 'PUPFIG83: DF, Variable hashing, 50% Train'
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'PUPFIG83: DF, Variable hashing, 90% Train'
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f PUPFIG83-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.9
