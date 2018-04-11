#!/bin/sh

echo 'executing convert_SRILM_output_json.sh'
date

module add openmind/miniconda/4.0.5-python3
python3 convert_SRILM_output_json.py

echo 'finished!'
date