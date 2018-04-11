#!/bin/bash
# python 2 is used for the following scripts

echo 'executing clean_txt.sh'
date
python xmlParser.py
python first_level_filter.py
python second_level_filter.py
rm -r ../first_level_clean_txt/
python third_level_filter.py
date
