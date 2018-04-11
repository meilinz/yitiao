#!/bin/sh
#SBATCH --ntasks=1
#SBATCH --time=4-00:00:00
#SBATCH --mem-per-cpu=20000
#SBATCH --qos=cpl
#SBATCH --output=./slurm_log/SRILM_5gram_unk_crossvalid-%j.out

echo 'executing SRILM_5gram_unk_crossvalid.sh'
date

NGRAMCOUNT="/srilm/bin/i686-m64/ngram-count"
NAGRAM="/srilm/bin/i686-m64/ngram"
CONTAINER="/om/user/meilinz/singularity_imported/SRILM.img"
VOCAB="/om/data/public/text-corpora/sogoucs-2008/SRILM_modeling/vocab/corpus.vocab"

module add openmind/singularity/2.3.1

a=0
while [ $a -lt 10 ]
do
	index=$a
	if [ "$a" -lt 10 ]
	then
		index=0$a
	fi
	echo 'starting the training process part '$index''
	singularity exec -B /om:/om $CONTAINER $NGRAMCOUNT -text ../train_data/train_file_$index -order 5 —kndiscount2 -kndiscount3 -kndiscount4 -kndiscount5 -unk -vocab $VOCAB -lm ../lang_models/5gram_kn_unk_train_file_$index.lm
	echo 'language model trained on part '$index''
	singularity exec -B /om:/om $CONTAINER $NAGRAM -order 5 -lm ../lang_models/5gram_kn_unk_train_file_$index.lm -unk -vocab $VOCAB -ppl ../test_data/test_file_$index -debug 2 > ../results/5gram_kn_unk_test_file_$index.probs
	echo 'finished testing on part '$index''
	date
	a=`expr $a + 1`
done

echo 'finished!'
date
