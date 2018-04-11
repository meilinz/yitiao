import csv, linecache, os

DBG = '-----> '

# 0 Create a hash table for txt file content
file_content_hash = {}

txtDir = '../tokenized_text_from_json/'
outputDir = '../cl_replaced_text/'
#file_name_prefix = 'news.sohunews.'
replacement = "CL"

## 1.1 Open csv file
with open('../classifier_data/cl_noun_clean.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	next(readCSV, None)
	for row in readCSV:
		# row is a list with coloumns shown below:
		# 0 num
		# 1 classifier
		# 2 noun
		# 3 sentence_token_num
		# 4 cl_token_num
		# 5 noun_token_num
		# 6 file_name

		## 1.2 parse each line in csv
		sentence_token_num = int(row[3])
		cl_token_num = int(row[4])
		file_name = ('.'.join(row[6].split('.')[:-1]) + ".token")

		line_number = sentence_token_num + 1
		element_number = cl_token_num - 1
		
		# print(sentence_token_num + ":" + cl_token_num + ":" + file_name)

  		## 1.3 [Optional] append the sentence to csv file (Skipped)

		## 2.1 Open txt file / Get txt content from hash table
		content = file_content_hash.get(file_name)
		if (content == None):
			file_path = txtDir + file_name
			fo = open(file_path, "r")

			content = fo.readlines()
			file_content_hash[file_name] = content
			print(DBG + "Opened " + file_path)

			fo.close()

		#print(DBG + "line at " + str(line_number) + " of " + file_path + " is :")
		targetLine = content[line_number-1]
		#print(DBG + targetLine)			
		
		## 2.2 replace tokens
		line_to_list = targetLine.split()
		line_to_list[element_number] = replacement
		line_changed = ' '.join(str(e) for e in line_to_list) + '\n'
		#print(DBG + line_changed)
		content[line_number-1] = line_changed
			
## 3 save new content to output files
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

for file_name, content in file_content_hash.items():
	#output_file_path = outputDir + file_name_prefix + file_name + ".modified"
	output_file_path = outputDir + file_name + ".modified"
	output_file = open(output_file_path, "w")
	for line in content:
  		output_file.write("%s" % line)
	output_file.close()
	print(DBG + "Saved " + output_file_path)