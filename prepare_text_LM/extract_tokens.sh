#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --time=5:00:00
#SBATCH --mem-per-cpu=4000
#SBATCH --qos=cpl
#SBATCH --output=./slurm_log/extract_tokens-%j.out

echo 'executing extract_tokens.sh'
date

module add openmind/miniconda/4.0.5-python3
python3 extract_tokens.py

echo 'finished!'
date