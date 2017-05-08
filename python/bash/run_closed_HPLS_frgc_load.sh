#!/bin/bash

#HOG
echo 'FRGC4: HOG, Variable hashing, 10% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC4: HOG, Variable hashing, 50% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC4: HOG, Variable hashing, 90% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

#DF
echo 'FRGC4: DF, Variable hashing, 10% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC4: DF, Variable hashing, 50% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC4: DF, Variable hashing, 90% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-4-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5


#HOG
echo 'FRGC1: HOG, Variable hashing, 10% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC1: HOG, Variable hashing, 50% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC1: HOG, Variable hashing, 90% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-HOG-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

#DF
echo 'FRGC1: DF, Variable hashing, 10% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC1: DF, Variable hashing, 50% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

echo 'FRGC1: DF, Variable hashing, 90% Known size, 50% Train/Test'
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 100 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 300 -ts 0.5
python ../HPLS_closedset_load.py -p ../features/ -f FRGC-SET-1-DEEP-FEATURE-VECTORS.bin -r 10 -m 500 -ts 0.5

