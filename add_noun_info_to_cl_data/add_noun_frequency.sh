#!/bin/bash

echo 'executing create_heldout.sh'
date

module add openmind/miniconda/4.0.5-python3
python3 create_heldout.py

echo 'finished!'
date