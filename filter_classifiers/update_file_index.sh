#!/bin/bash

echo 'executing update_file_index.sh'
date

module add openmind/anaconda/2.5.0
python3 update_file_index.py

echo 'finished!'
date