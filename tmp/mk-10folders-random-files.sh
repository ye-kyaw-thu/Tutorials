#!/bin/bash

# written by ye
# bash script exercise demo @Summer Schools 2018
# Simulation of class folders and random file generations


# building 10 class folders
for number in {1..10}
#for number in {1..$1}
do
   #echo $number
   mkdir ./class$number;
   
   #Generate random number
   random_number="$(shuf -i 1-100 -n1)"
   echo "start making $random_number files";
#   if [ $random_number -eq 1 ];
#      then
#         $random_number++;
#   fi

   #file generation based on random number
   #for (( 1; fno<=$random_number; fno++ ))
   for fno in $( seq 1 $random_number )
   do
      touch ./class$number/file_$fno;
      echo $(date +%s%N) >> ./class$number/file_$fno;
      pwd >> ./class$number/file_$fno;
   done
done
exit 0
