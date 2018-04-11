#!/bin/bash

echo 'executing merge_csv.sh'
date

module add openmind/miniconda/4.0.5-python3
python3 merge_csv.py

echo 'finished!'
date
