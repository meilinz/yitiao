import os, json

corpus = []
unique_sentences = {}

with open('../deduplication/entire_corpus', 'r') as text_input:
#with open('../test_short', 'r') as text_input:

	content = text_input.read()
	with open('../deduplication/entire_corpus_deduplicated', 'w') as text_output:
	#with open('../test_deduplicated', 'w') as text_output:
		
		for line in content.splitlines():
			if not line in unique_sentences:
				unique_sentences[line] = 1
				corpus.append(line)
			else:
				unique_sentences[line] = unique_sentences[line] + 1

		print('start writing files')

		for item in corpus:
			text_output.write("%s\n" % item)

		json_str = json.dumps(unique_sentences, ensure_ascii=False, indent=4, separators=(',', ': '))

		with open('../deduplication/sentence_counts.json', 'w') as output_json:
			output_json.write(json_str)

print('finished!')