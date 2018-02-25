#!/bin/bash

#How to run:
#./tst.sh <gaussian-model-filename> <test-image-filename>
#e.g. ./tst.sh ./mc-mdy.4096.model ./MVI_8489-C_39-Ka_41.jpg
#e.g. ./tst.sh ./mc-mdy.4096.model ./IdxF-35_01-Ah_1.jpg

#If you want to print out only class dictionary, run as follow:
# ./tst.sh ./mc-mdy.4096.model ./MVI_8489-C_39-Ka_41.jpg 2>&1 | tail -n 1

# feature extraction for input image file
python get-input-image-feature.py $2


# Changing column to row with delimiter comma and removing the last comma
filename=$(basename $2)
filename="${filename%.*}"

tr '\n' ',' < $filename.f | sed 's/.$//' > $filename.f.clean

# classification of input test png file

python ./test-model.py $1 $filename.f.clean

