# This code is used for extracting classifier-noun pairs from a corpus
# Meilin Zhan, July 14, 2017

import json, os, csv

def extract(fileName, filePath, outputDir):

	outputFile = outputDir + '/' + fileName + '.csv'

	with open(filePath) as f:
		data = json.load(f)

	sentences = data["sentences"]
	head_noun = []
	dep_classifier = []
	num_word = []
	sentence_index = []
	cl_token_index = []
	noun_token_index = []

	for i in range(len(sentences)):
		try:
			for j in range(len(sentences[i]["basicDependencies"])):
				if sentences[i]["basicDependencies"][j]['dep'] == "nummod":
					if sentences[i]["basicDependencies"][j+1]["dep"] == "mark:clf":
						head_noun.append(sentences[i]["basicDependencies"][j]["governorGloss"])
						dep_classifier.append(sentences[i]["basicDependencies"][j+1]["dependentGloss"])
						num_word.append(sentences[i]["basicDependencies"][j+1]["governorGloss"])
						sentence_index.append(i)
						cl_token_index.append(sentences[i]["basicDependencies"][j+1]["dependent"])
						noun_token_index.append(sentences[i]["basicDependencies"][j]["governor"])
		except:
			pass

	with open(outputFile, 'w', newline="") as fo:
		writer = csv.writer(fo)
		writer.writerows(zip(num_word, dep_classifier, head_noun, sentence_index, cl_token_index, noun_token_index))

	print ("Saved {0}".format(outputFile))
	return

def main():

	rawDataDir = '../stanford_corenlp_json_output'
	outputDir = '../classifier_noun_pairs'

	if not os.path.exists(outputDir):
		os.makedirs(outputDir)

	for file in os.listdir(rawDataDir):
		if file.endswith(".json"):
			fileName = '.'.join(file.split('.')[:-1])
			filePath = os.path.join(rawDataDir, file)
			extract(fileName, filePath, outputDir)

if __name__ == "__main__":
	main()


