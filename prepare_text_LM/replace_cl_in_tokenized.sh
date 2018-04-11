#!/bin/bash

echo 'executing replace_cl_in_tokenized.sh'
date

module add openmind/miniconda/4.0.5-python3
python3 replace_cl_in_tokenized.py

echo 'finished!'
date
