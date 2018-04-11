# -*- coding: utf-8 -*-
import re, os, sys
import codecs
reload(sys) 
sys.setdefaultencoding('utf8')

def clean(fileName, filePath, outputDir):

	outputFile = outputDir + '/' + fileName + '.clean'
	fo = open(outputFile, "wb")

	with codecs.open(filePath, 'r', encoding='utf8') as f:
		lines = f.read()

	items = []
	# write the filter conditions here
	line_break = re.compile(u'\n')
	period = re.compile(u'。')
	excl = re.compile(u'！')
	question = re.compile(u'？')
	for line in lines.splitlines():
		line = re.sub(line_break, '', line)
		line = re.sub(period, u'。\n', line)
		line = re.sub(excl, u'！\n', line)
		line = re.sub(question, u'？\n', line)

		items.append(line)

		for sentence in line.splitlines():
			if len(sentence) >3 and len(sentence)<= 120:
				fo.write(sentence.encode('utf-8'))
				fo.write('\n')

	fo.close()
	print '[Saved]' + outputFile

	return items


def main():

	rawDataDir = '../second_level_clean_txt'
	outputDir = '../third_level_clean_txt'

	if not os.path.exists(outputDir):
		os.makedirs(outputDir)

	for file in os.listdir(rawDataDir):
		if file.endswith(".clean"):
			fileName = '.'.join(file.split('.')[:-1])
			filePath = os.path.join(rawDataDir, file)
			items = clean(fileName, filePath, outputDir)

if __name__ == "__main__":

	main()