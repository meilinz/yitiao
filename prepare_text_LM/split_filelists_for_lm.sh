#!/bin/bash

echo 'split_filelists_for_lm.sh'
date

mkdir ../SRILM_modeling/concatenated_files/ || echo "../SRILM_modeling/concatenated_files/ exists"
mkdir ../SRILM_modeling/test_data/ || echo "../SRILM_modeling/test_data/ exists"

#readlink -f ../cl_replaced_text/*.token.modified > ../SRILM_modeling/filelists/filelist_fullpath_for_lm
#split -d -l 40 ../SRILM_modeling/filelists/filelist_fullpath_for_lm ../SRILM_modeling/filelists/filelist_

a=0
while [ $a -lt 10 ]
do
	index=$a
	if [ "$a" -lt 10 ]
	then
	    index=0$a
	fi
	xargs < ../SRILM_modeling/filelists/filelist_$index cat > ../SRILM_modeling/concatenated_files/file_$index
	echo $index
	a=`expr $a + 1`
done

a=0
while [ $a -lt 10 ]
do
	index=$a
	if [ "$a" -lt 10 ]
	then
	    index=0$a
	fi
	cp ../SRILM_modeling/filelists/filelist_$index ../SRILM_modeling/filelists/test_filelist_$index
	echo $index
	a=`expr $a + 1`
done

a=0
while [ $a -lt 10 ]
do
	index=$a
	if [ "$a" -lt 10 ]
	then
	    index=0$a
	fi
	cp ../SRILM_modeling/concatenated_files/file_$index ../SRILM_modeling/test_data/test_file_$index
	echo $index
	a=`expr $a + 1`
done

a=0
while [ $a -lt 10 ]
do
	index=$a
	if [ "$a" -lt 10 ]
	then
	    index=0$a
	fi
	xargs < ../SRILM_modeling/filelists/train_filelist_$index cat > ../SRILM_modeling/train_data/train_file_$index
	echo $index
	a=`expr $a + 1`
done


echo 'finished!'
date