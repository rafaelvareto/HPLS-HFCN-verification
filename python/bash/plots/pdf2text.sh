#!/bin/bash

# sudo apt-get install poppler-utils

for filename in `ls -d -1 $1/*.pdf`
do
	pdftotext $filename `echo $filename | sed -e 's/pdf/txt/g'`
done
