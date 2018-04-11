# -*- coding: utf-8 -*-
import re, os, sys
reload(sys) 
sys.setdefaultencoding('utf8')

def clean(fileName, filePath, outputDir):

	outputFile = outputDir + '/' + fileName + '.txt'
	fo = open(outputFile, "wb")

	with file(filePath) as f:
		string = f.read()

	items = []
	# write the filter conditions here
	#junk_word = re.compile('?（.+）|^.+?讯　(（记者.+?）)?(　)?|^.+?讯（记者.+?）|^.+?消息　(（记者.+?）)?|^.+?消息（记者.+）|^.+电　(（记者.+?）)?(　)?|^.+?电（记者.+?）|（.+?）|［.+?］(　)?|【.+】(：)?(　)?|⊙|跳转至.*|?精彩图片|您所要访问的房源信息不存在或已被删除！|您要对您发表的言论之后果负责，故请各位遵纪守法并注意语言文明！|本网站提供之资料或信息，仅供投资者参考，不构成投资建议。|搜狐证券声明：本频道资讯内容系转引自合作媒体及合作机构，不代表搜狐证券自身观点与立场，建议投资者对此资讯谨慎判断，据此入市，风险自担。|注：此为该公司赔率数据，比赛前有可能发生变化，敬请关注。')
	junk_word = re.compile('^.+?讯　(（记者.+?）)?(　)?|^.+?讯（记者.+?）|^.+?消息　(（记者.+?）)?|^.+?消息（记者.+）|^.+电　(（记者.+?）)?(　)?|^.+?电（记者.+?）|（.+?）|［.+?］(　)?|【.+】(：)?(　)?|⊙|跳转至.*|?精彩图片|您所要访问的房源信息不存在或已被删除！|您要对您发表的言论之后果负责，故请各位遵纪守法并注意语言文明！|本网站提供之资料或信息，仅供投资者参考，不构成投资建议。|搜狐证券声明：本频道资讯内容系转引自合作媒体及合作机构，不代表搜狐证券自身观点与立场，建议投资者对此资讯谨慎判断，据此入市，风险自担。|注：此为该公司赔率数据，比赛前有可能发生变化，敬请关注。')

	#is_sentence = re.compile('^.+$')
	for line in string.splitlines():
		line = re.sub(junk_word, '', line)
		line = re.sub('', '\n', line)
		#line = re.sub('　', '\n', line)
		items.append(line)
		fo.write(line.encode('utf-8'))
		fo.write('\n')

	fo.close()
	print '[Saved]' + outputFile

	return items


def main():

	rawDataDir = '../raw_text' # change input dir here
	outputDir = '../first_level_clean_txt' # change output dir here

	if not os.path.exists(outputDir):
		os.makedirs(outputDir)

	for file in os.listdir(rawDataDir):
		if file.endswith(".txt"):
			fileName = '.'.join(file.split('.')[:-1])
			filePath = os.path.join(rawDataDir, file)
			items = clean(fileName, filePath, outputDir)

if __name__ == "__main__":

	main()