import csv, os

# use a dictionary to store word frequency
counts = {}
with open('../tokenized_corpus', 'r') as corpus:
    text = corpus.read()

for word in text.split():
    if not word in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word] + 1

print('finished counting words!')

# find word frequency for the nouns and add it to the csv
with open('../classifier_data/classifiers_20171121.csv', 'r') as csvInput:
    with open('../classifier_data/classifiers_20171122.csv', 'w') as csvOutput:
        writerCSV = csv.writer(csvOutput)
        readCSV = csv.reader(csvInput, delimiter=',')

        everthing = []
        row = next(readCSV)
        row.append('noun_freq')
        everthing.append(row)

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
		# 12 noun_prob (in context noun probability)
            
            noun = row[2]

            noun_freq = int(counts[noun])

            row.append(noun_freq)
            everthing.append(row)

        writerCSV.writerows(everthing)



