#!/bin/bash

# for image feature extraction with CNN model
# written by Ye Kyaw Thu, OPU, Japan
#How to run: ./extract-feature.sh ./data/

folder_list_array=($(find "$1" -maxdepth 1 -type d))

total=${#folder_list_array[*]}
echo $total;
# 
for (( i=1; i<=$(( $total -1 )); i++ ))
do 
    echo -n "Start working on folder: ${folder_list_array[$i]} "
    python ./feature.py "${folder_list_array[$i]}"
done
