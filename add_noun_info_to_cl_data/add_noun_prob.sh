#!/bin/bash

echo 'executing add_noun_prob.sh'
date

module add openmind/miniconda/4.0.5-python3
python3 add_noun_prob.py

echo 'finished!'
date