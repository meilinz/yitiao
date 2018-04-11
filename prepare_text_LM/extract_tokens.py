import json, os, re

def extractTokens(fileName, filePath, outputDir):

	outputFile = outputDir + '/' + fileName + '.token'
	fo = open(outputFile, "w")

	with open(filePath) as f:
		data = json.load(f)

	sentences = data["sentences"]

	for sentence in sentences:
		tokenized_sentence = []

		for token in sentence["tokens"]:
			tokenized_sentence.append(token["word"])

		line = ' '.join(tokenized_sentence)
		fo.write(line)
		fo.write("\n")

	fo.close()

	print ("Saved {0}".format(outputFile))
	
	return


def main():

	rawDataDir = '../stanford_corenlp_json_output'
	outputDir = '../tokenized_text_from_json'

	if not os.path.exists(outputDir):
		os.makedirs(outputDir)

	for file in os.listdir(rawDataDir):
		if file.endswith(".json"):
			fileName = '.'.join(file.split('.')[:-1])
			filePath = os.path.join(rawDataDir, file)
			extractTokens(fileName, filePath, outputDir)

if __name__ == "__main__":
	main()