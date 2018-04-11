#!/bin/sh

echo 'executing file_index.sh'
date

module add openmind/miniconda/4.0.5-python3
python3 file_index.py

echo 'finished!'
date