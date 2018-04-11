#!/bin/bash

index=$1

echo 'executing stanford_corenlp_filelist_'$index'.sh'
date

java -mx9g -cp "/om/data/public/text-corpora/stanford-corenlp-full-2017-06-09/*" edu.stanford.nlp.pipeline.StanfordCoreNLP -props StanfordCoreNLP-chinese.properties -annotators tokenize,ssplit,pos,parse -filelist /om/data/public/text-corpora/sogoucs-2008/deduplication/filelists/for_parsing/filelist_$index -outputFormat json -outputDirectory /om/data/public/text-corpora/sogoucs-2008/stanford_corenlp_json_output/ -replaceExtension

echo 'finished!'
date