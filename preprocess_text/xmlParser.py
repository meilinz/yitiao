# This Python file uses the following encoding: utf-8
from lxml import etree
import os

def parseXML(fileName, filePath, outputDir):

    outputFile = outputDir + '/' + fileName + '.txt'
    fo = open(outputFile, "wb")

    with file(filePath) as f:
        xmlstring = "<root>" + f.read() + "</root>"
        parser = etree.XMLParser(recover=True, encoding='gb18030')
        xmlItems = etree.fromstring(xmlstring, parser=parser)

    docItems = []
    for doc in xmlItems.findall('doc'):
        # Put your tag here, for example, './/content' for <content>
        content = doc.find('.//content').text
        try:
            docItems.append(content)
            fo.write(content.encode('utf-8'))
            fo.write('\n')
        except:
            pass

    fo.close()
    print '[Saved] ' + outputFile

    return docItems


def main():

    rawDataDir = '/om/data/public/text-corpora/sogoucs-2008/raw_data'
    outputDir = '/om/data/public/text-corpora/sogoucs-2008/raw_text'

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for file in os.listdir(rawDataDir):
        if file.endswith(".txt"):
            fileName = '.'.join(file.split('.')[:-1])
            filePath = os.path.join(rawDataDir, file)
            docItems = parseXML(fileName, filePath, outputDir)

if __name__ == "__main__":

    # calling main function
    main()