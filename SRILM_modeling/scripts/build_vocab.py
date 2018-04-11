import os

min_count = 1
vocabulary = []

def buildVocab(fileName, filePath, outputDir):

    outputFile = outputDir + '/' + fileName + '.vocab'

    with open(filePath, 'r') as input_count:
        for line in input_count:
            word_itself = line.split('\t')[0]
            word_count = int(line.split('\t')[1])
            if word_count > min_count:
                vocabulary.append(word_itself)
    
    with open(outputFile, 'w') as output_vocab:
        for item in vocabulary:
            output_vocab.write("%s\n" % item)

    return

def main():

	rawDataDir = '../vocab'
	outputDir = '../vocab'

	if not os.path.exists(outputDir):
		os.makedirs(outputDir)

	for file in os.listdir(rawDataDir):
		if file.endswith(".count"):
			fileName = '.'.join(file.split('.')[:-1])
			filePath = os.path.join(rawDataDir, file)
			buildVocab(fileName, filePath, outputDir)

if __name__ == "__main__":
	main()

