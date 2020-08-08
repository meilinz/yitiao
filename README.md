# yitiao
Code for extracting and analyzing classifier-noun pairs from a Mandarin Chinese corpus

The raw data (SogouCS, 2008 version) is from Sogou Labs accessible via https://www.sogou.com/labs/resource/cs.php (Look for the 2008 version). The processed data and analysis code are available at https://osf.io/8zwrm/. 

The pipeline follows the order specified below. Some code are wrapped in a bash script. You may need to modify the input and output folders for your specific folder structure. 


1. preprocess_text/
    - xmlParser.py
    - clean_text.sh
        - first_level_filter.py
        - second_level_filter.py
        - third_level_filter.py
    - deduplicate_sentences.sh
        - deduplicate_sentences.py

2. parse_text/
    - split_filelists_for_parsing.sh 
    - stanford_corenlp.sh
    - extract_cl_noun.sh
        - extract_cl_noun.py
    - merge_csv.sh
        - merge_csv.py


3. prepare_text_LM/
    - split_filelists_for_lm.sh
    - extract_tokens.sh
        - Extract_tokens.py
    - replace_cl_in_tokonized.sh
        - replace_cl_in_tokonized.py
4. SRILM_modeling/
    - scripts/file_index.sh
        - scripts/file_index.py
    - build_vocab.sh
        - build_vocab.py
    - SRILM_5gram_unk_crossvalid.sh
    - convert_SRILM_output_json.sh
        - convert_SRILM_output_json.py
5. filter_classifiers/
    - filter_cl_noun.sh
        - clean_cl_noun.R
        - filter_cl_noun.R
    - update_file_index.sh
        - update_file_index.py
6. add_noun_info_to_cl_data/
    - add_noun_prob.sh
        - add_noun_prob.py
    - add_noun_frequency.sh
        - add_noun_frequency.py
