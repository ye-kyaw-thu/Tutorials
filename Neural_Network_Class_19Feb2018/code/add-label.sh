#!/bin/bash
#Written by Ye Kyaw Thu, AI Lab., OPU
#Last updated: 6 Sept 2017
#How to run: ./add-label.sh ./data/

#For what: Combining features of all training image files into one file
#Note: Before running this shell script, you should run extract-feature.sh in advance


folder_list_array=($(find "$1" -maxdepth 1 -type d))
total=${#folder_list_array[*]}
#echo $total;

#removing dictionary file: id-name.txt 
if [ -f "$1/id-name.txt" ] 
then 
   rm $1/id-name.txt;
fi

#removing all-object-feature file
find "$1/" -name $(basename $1).feature -type f -exec rm '{}' \;
 
for (( i=1; i<=$(( $total -1 )); i++ ))
do 

   #search *.f files and put into array
   file_list_array=($(find ${folder_list_array[$i]} -type f -name "*.f"))

   #remove one object features file (e.g. totoro.feature, emo.feature)
   find "${folder_list_array[$i]}/" -name $(basename ${folder_list_array[$i]}).feature -type f -exec rm '{}' \;

   #find "${folder_list_array[$i]}/" -name $(basename ${folder_list_array[$i]}).f -type f -exec echo "Found!: " {} \; 

   file_total=${#file_list_array[*]}
   #echo "total no. of file:".$file_total;
   for (( j=0; j<=$(( $file_total-1 )); j++))
   do
      id_name=$i"\t"$(basename ${folder_list_array[$i]})
      cat ${file_list_array[$j]} | tr '\n' ',' | xargs -I {} echo {}$i >> "${folder_list_array[$i]}/tmp.feature" 
   done
   big_feature_file="${folder_list_array[$i]}/"$(basename ${folder_list_array[$i]}).feature

   
   mv "${folder_list_array[$i]}/tmp.feature" $big_feature_file
   echo -e "$id_name" >> "$1/id-name.txt"
   cat $big_feature_file >> $1/$(basename $1).feature
done

