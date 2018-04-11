import csv, os, json

DBG = '-----> '

# create a hash table for json file content
file_content_hash = {}

jsonDir = '../SRILM_modeling/results/output_dir_json/'

with open('../classifier_data/cl_noun_cl_prop_filtered_20171121.csv', 'r') as csvinput:
    with open('../classifier_data/classifiers_20171121.csv', 'w') as csvoutput:
        writerCSV = csv.writer(csvoutput)
        readCSV = csv.reader(csvinput, delimiter=',')

        everything = []
        row = next(readCSV)
        row.append('noun_prob')
        everything.append(row)

        for row in readCSV:
		# row is a list with coloumns shown below:
		# 0 num
		# 1 classifier
		# 2 noun
		# 3 sentence_token_num (starting from 0 for each document)
		# 4 cl_token_num (starting from 1 for each sentence)
		# 5 noun_token_num (starting from 1 for each sentence)
		# 6 file_name (e.g., file_aa, 40 in total)
		# 7 cl_freq_for_noun
		# 8 cl_prop_for_noun (before filtering)
		# 9 lm_file (file name of language modeling test file, e.g., file_00, 10 in total)
		# 10 sent_base (updated starting sentence index for each orginal document after they merged and become lm file)
		# 11 sent_index_lm_file (updated sentence index in the lm file, starting from 0)

		    ## parse each line in csv
            sentence_index = int(row[11])
            file_name = ('5gram_kn_unk_test_' + row[9] + '.json')
            noun_index = int(row[5]) - 1

            ## open json file / get json content from hash table
            content = file_content_hash.get(file_name)
            if (content == None):
                file_path = jsonDir + file_name
                fo = open(file_path, 'r')

                content = json.load(fo)
                file_content_hash[file_name] = content
                print(DBG + 'Opened' + file_path)

                fo.close()

            noun_prob = float(content['sentences'][sentence_index]['tokens'][noun_index]['prob'])

            ## append  noun probability to csv file 
            row.append(noun_prob)
            everything.append(row)

        writerCSV.writerows(everything)

