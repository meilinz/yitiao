#!/bin/bash

CONTAINER="/om/user/meilinz/singularity_imported/r-base.img"
module add openmind/singularity/2.3.1

echo 'executing filter_cl_noun.sh'
date

echo 'step 1: running clean_cl_noun.R'
singularity exec -B /om:/om $CONTAINER Rscript clean_cl_noun.R

echo 'step 2: running filter_cl_noun.R'
date
singularity exec -B /om:/om $CONTAINER Rscript filter_cl_noun.R

echo 'finished!'
date