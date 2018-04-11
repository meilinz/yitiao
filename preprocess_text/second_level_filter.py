# -*- coding: utf-8 -*-
import re, os, sys
reload(sys) 
sys.setdefaultencoding('utf8')

def clean(fileName, filePath, outputDir):

	outputFile = outputDir + '/' + fileName + '.clean'
	fo = open(outputFile, "wb")

	with file(filePath) as f:
		string = f.read()

	items = []
	# write the filter conditions here
	is_sentence = re.compile('^.+。$|^.+？$|^.+！$')
	for line in string.splitlines():
		if re.match(is_sentence, line):
			items.append(line)
			fo.write(line.encode('utf-8'))
			fo.write('\n')

	fo.close()
	print '[Saved]' + outputFile

	return items


def main():

	rawDataDir = '../first_level_clean_txt'
	outputDir = '../second_level_clean_txt'

	if not os.path.exists(outputDir):
		os.makedirs(outputDir)

	for file in os.listdir(rawDataDir):
		if file.endswith(".txt"):
			fileName = '.'.join(file.split('.')[:-1])
			filePath = os.path.join(rawDataDir, file)
			items = clean(fileName, filePath, outputDir)

if __name__ == "__main__":

	main()