#!/bin/bash

split -l 28884 ../deduplication/entire_corpus_deduplicated ../deduplication/files/file_

readlink -f ../deduplication/files/file_* > ../deduplication/filelists/filelist_fullpath

mkdir ../deduplication/filelists/for_parsing/

split -d -l 20 ../deduplication/filelists/filelist_fullpath ../deduplication/filelists/for_parsing/filelist_
