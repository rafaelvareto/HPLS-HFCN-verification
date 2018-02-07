#!/bin/bash

#DF
echo 'PUBFIG-DEV, LFW: DF, Hash_samples = 50, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 005 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 010 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 020 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 030 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 050 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 070 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 100 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 300 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 500 -hs 50 -it 10

echo 'PUBFIG-DEV, LFW: DF, Hash_samples = 100, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 005 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 010 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 020 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 030 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 050 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 070 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 100 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 300 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 500 -hs 100 -it 10

echo 'PUBFIG-DEV, LFW: DF, Hash_samples = 300, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 005 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 010 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 020 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 030 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 050 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 070 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 100 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 300 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 500 -hs 300 -it 10

echo 'PUBFIG-DEV, LFW: DF, Hash_samples = 500, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 005 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 010 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 020 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 030 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 050 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 070 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 100 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 300 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/lfw/lfw_pairs.txt -d lfw -ftr PUBFIG-DEV-DEEP.bin -fts LFW-DEEP.bin -hm 500 -hs 500 -it 10


#DF
echo 'PUBFIG-DEV, PUBFIG-EVAL: DF, Hash_samples = 50, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 005 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 010 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 020 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 030 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 050 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 070 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 100 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 300 -hs 50 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 500 -hs 50 -it 10

echo 'PUBFIG-DEV, PUBFIG-EVAL: DF, Hash_samples = 100, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 005 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 010 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 020 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 030 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 050 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 070 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 100 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 300 -hs 100 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 500 -hs 100 -it 10

echo 'PUBFIG-DEV, PUBFIG-EVAL: DF, Hash_samples = 300, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 005 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 010 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 020 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 030 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 050 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 070 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 100 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 300 -hs 300 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 500 -hs 300 -it 10

echo 'PUBFIG-DEV, PUBFIG-EVAL: DF, Hash_samples = 500, Iterations = 10'
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 005 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 010 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 020 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 030 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 050 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 070 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 100 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 300 -hs 500 -it 10
python ../HPLS_verification_cross_load.py -p ../features/ -c ../datasets/pubfig/pubfig_full.txt -d pubfig -ftr PUBFIG-DEV-DEEP.bin -fts PUBFIG-EVAL-DEEP.bin -hm 500 -hs 500 -it 10
