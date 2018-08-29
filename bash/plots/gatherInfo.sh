#!/bin/bash

# sudo apt-get install poppler-utils

for filename in `ls -d -1 $1/*.txt`
do
	grep "Receiver Operating Characteristic" $filename echo $filename
done
