#!/bin/bash

for file in *.txt; do
    # exit if there are no .txt files
    if [ ! -f $file ]; then
        exit
    fi

    b=`basename $file .txt`
    
    soffice --convert-to jpg $b.txt 2> /dev/null
    echo ""

done
