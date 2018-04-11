import os, re, json

def extract(fileName, filePath, outputDir):

	outputFile = outputDir + '/' + fileName + '.json'

	with open(filePath) as f:
		content = f.read()
		sentence_blocks = content.split('\n\n')
		sentences_json = []

		for sentence_index in range(0, len(sentence_blocks)-1):
			sentence = sentence_blocks[sentence_index]
			lines = sentence.split('\n')
			lines_num = len(lines)

			sentence_text = lines[0]
			sentence_OOV = int(lines[lines_num - 2].split(' ')[4])
			sentence_sentenceLogprob = lines[lines_num - 1].split(' ')[3]
			sentence_sentencePpl = lines[lines_num -1].split(' ')[5]
			sentence_sentencePpl1 = lines[lines_num -1].split(' ')[7]

			sentence_tokens = []

			for token_line_index in range(1, lines_num-3):
				token_line = lines[token_line_index]
				token_line_split_items = token_line.split(' ')

				token_index = token_line_index
				token_word = token_line_split_items[1]
				raw_cxt = token_line_split_items[6]
				token_cxt = raw_cxt[1 : len(raw_cxt)-1]
				token_prob = token_line_split_items[7]#change it to 9 for logprob

				sentence_token = {}
				sentence_token["index"] = token_index
				sentence_token["word"] = token_word
				sentence_token["prob"] = token_prob
				sentence_token["cxt"] = token_cxt

				sentence_tokens.append(sentence_token)

			sentence_json = {}
			sentence_json["index"] = sentence_index
			sentence_json["text"] = sentence_text
			sentence_json["sentenceLogprob"] = sentence_sentenceLogprob
			sentence_json["sentencePpl"] = sentence_sentencePpl
			sentence_json["sentencePpl1"] = sentence_sentencePpl1
			sentence_json["OOV"] = sentence_OOV
			sentence_json["tokens"] = sentence_tokens

			sentences_json.append(sentence_json)

	doc_info = sentence_blocks[len(sentence_blocks)-1].split('\n')
	doc_info_file = doc_info[0]
	doc_info_perplexity = doc_info[1]

	processed_sentences = {}

	doc_info= {}
	doc_info["file"] = doc_info_file
	doc_info["perplexity"] = doc_info_perplexity

	processed_sentences["doc_info"] = doc_info
	processed_sentences["sentences"] = sentences_json

	json_str = json.dumps(processed_sentences, ensure_ascii=False, indent=4, separators=(',', ': '))
	
	output = open(outputFile, "w") 
	output.write(json_str) 	
	output.close() 

	print ("Saved {0}".format(outputFile))
	return

def main():

	rawDataDir = '../results'
	outputDir = '../results/output_dir_json'

	if not os.path.exists(outputDir):
		os.makedirs(outputDir)

	for file in os.listdir(rawDataDir):
		if file.endswith(".probs"):
			fileName = '.'.join(file.split('.')[:-1])
			filePath = os.path.join(rawDataDir, file)
			extract(fileName, filePath, outputDir)

if __name__ == "__main__":
	main()