#!/bin/bash

#HOG
echo 'FRGC4: HOG, Variable hashing, 10% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.1

echo 'FRGC4: HOG, Variable hashing, 50% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC4: HOG, Variable hashing, 90% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.9

#DF
echo 'FRGC4: DF, Variable hashing, 10% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.1

echo 'FRGC4: DF, Variable hashing, 50% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC4: DF, Variable hashing, 90% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.9


#HOG
echo 'FRGC1: HOG, Variable hashing, 10% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.1

echo 'FRGC1: HOG, Variable hashing, 50% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC1: HOG, Variable hashing, 90% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.9

#DF
echo 'FRGC1: DF, Variable hashing, 10% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.1
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.1

echo 'FRGC1: DF, Variable hashing, 50% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC1: DF, Variable hashing, 90% Train'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.9
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.9

