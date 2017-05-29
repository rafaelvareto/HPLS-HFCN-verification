#!/bin/bash

#DF
echo 'PUBFIG-DEV, LFW: DF, Hash_samples = 100, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 100 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 300 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 500 -hs 100 -it 10

echo 'PUBFIG-DEV, LFW: DF, Hash_samples = 300, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 100 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 300 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 500 -hs 300 -it 10

echo 'PUBFIG-DEV, LFW: DF, Hash_samples = 500, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 100 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 300 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 500 -hs 500 -it 10

