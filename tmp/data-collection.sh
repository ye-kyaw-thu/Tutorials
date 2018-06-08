#!/bin/bash

# written by ye
# bash script exercise demo @Summer Schools 2018
# for making simlation of handwritting data collection on x PC
# how to run: ./data-collection.sh no_of_pc
# e.g. if you want to simulate handwritting data collection with 10 pc: ./data-collection.sh 10


# reading command line argument for no. of running machines
pc=$1;
echo -e "Data collection on $pc PC\n";

for no_of_pc in $( seq 1 $pc )
do

   mkdir pc$no_of_pc;
   cd pc$no_of_pc;
   ../mk-10folders-random-files.sh;
   cd ..;

done
