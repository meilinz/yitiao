#!/bin/sh

echo 'executing build_vocab.sh'
date

NGRAMCOUNT="/srilm/bin/i686-m64/ngram-count"
NAGRAM="/srilm/bin/i686-m64/ngram"
CONTAINER="/om/user/meilinz/singularity_imported/SRILM.img"
TRAINFILENAME="/om/data/public/text-corpora/sogoucs-2008/SRILM_modeling/concatenated_files/sogoucs-2008_deduplicated_tokenized"

module add openmind/singularity/2.3.1
module add openmind/miniconda/4.0.5-python3

echo 'starting counting words'
singularity exec -B /om:/om $CONTAINER $NGRAMCOUNT -text $TRAINFILENAME -order 1 -write ../vocab/corpus.count

echo 'starting building vocabulary'
python3 build_vocab.py

echo 'finished!'
date