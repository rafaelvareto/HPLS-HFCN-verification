#!/bin/bash

#DF
echo 'LFW: DF, Hash_samples = 100, Iterations = 10'
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 100 -hs 100 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 300 -hs 100 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 500 -hs 100 -it 10

echo 'LFW: DF, Hash_samples = 300, Iterations = 10'
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 100 -hs 300 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 300 -hs 300 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 500 -hs 300 -it 10

echo 'LFW: DF, Hash_samples = 500, Iterations = 10'
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 100 -hs 500 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 300 -hs 500 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -f LFW-DEEP.bin -hm 500 -hs 500 -it 10


#DF
echo 'PUBFIG-EVAL: DF, Hash_samples = 100, Iterations = 10'
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -f PUBFIG-EVAL-DEEP.bin -hm 100 -hs 100 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -f PUBFIG-EVAL-DEEP.bin -hm 300 -hs 100 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -f PUBFIG-EVAL-DEEP.bin -hm 500 -hs 100 -it 10

echo 'PUBFIG-EVAL: DF, Hash_samples = 300, Iterations = 10'
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -f PUBFIG-EVAL-DEEP.bin -hm 100 -hs 300 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -f PUBFIG-EVAL-DEEP.bin -hm 300 -hs 300 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -f PUBFIG-EVAL-DEEP.bin -hm 500 -hs 300 -it 10

echo 'PUBFIG-EVAL: DF, Hash_samples = 500, Iterations = 10'
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -f PUBFIG-EVAL-DEEP.bin -hm 100 -hs 500 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -f PUBFIG-EVAL-DEEP.bin -hm 300 -hs 500 -it 10
python ../HPLS_verification_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -f PUBFIG-EVAL-DEEP.bin -hm 500 -hs 500 -it 10
