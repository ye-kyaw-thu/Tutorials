#!/bin/bash

# written by ye
# bash script exercise demo @Summer Schools 2018
# Grouping/Collecting all collected handwriting data

# prepare a new folder and 10 sub-folders for combining all collected data
mkdir -p all-data/{class1,class2,class3,class4,class5,class6,class7,class8,class9,class10};

parent_path=$(pwd);
FID=1;
# copying all files of each pc
for folder in */
do
   echo -e "Start working on $folder ...\n";
   if [[ "$folder" != "all-data/" ]]; then
   
      cd $folder;
      pwd;

      for subfolder in */
      do
         echo -e "\nEntering into $subfolder folder!\n";
         cd $subfolder; 
         for image_file in *
         do
            echo -e "coping $image_file image file...";
            cp $image_file $parent_path/all-data/$subfolder$image_file"_"$FID;
            FID=$(($FID+1));
         done
         cd ..; 
         #pwd;
      done
      cd ..;
      #pwd; exit;
   fi
done




