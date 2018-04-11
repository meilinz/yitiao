#!/bin/bash

echo 'executing extract_cl_noun.sh'
date

module add openmind/miniconda/4.0.5-python3
python3 extract_cl_noun.py

echo 'finished!'
date