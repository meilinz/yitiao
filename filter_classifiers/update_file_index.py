import pandas as pd
with open('../classifier_data/cl_noun_cl_prop_filtered.csv', 'r') as file_in:
	filedata = file_in.read()

filedata = filedata.replace('.csv', '')

with open('../classifier_data/cl_noun_cl_prop_filtered_20171121.csv', 'w') as file_out:
	file_out.write(filedata)

data = pd.read_csv('../classifier_data/cl_noun_cl_prop_filtered_20171121.csv')
index = pd.read_csv('../SRILM_modeling/filelists/file_index.csv')

merged = data.merge(index, on = 'file_name')
merged = merged.drop('lines', axis = 1)
merged['sent_index_lm_file'] = merged['sentence_token_num'] + merged ['sent_base']

merged.to_csv('../classifier_data/cl_noun_cl_prop_filtered_20171121.csv', index = False)
