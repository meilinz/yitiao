#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=12000
#SBATCH --qos=cpl
#SBATCH --output=./slurm_log/deduplicate_sentences-%j.out
#SBATCH --mail-type=END
#SBATCH --maile-user=meilinz@mit.edu


echo 'executing deduplicate_sentences.sh'
date

module add openmind/miniconda/4.0.5-python3
python3 deduplicate_sentences.py

echo 'finished!'
date