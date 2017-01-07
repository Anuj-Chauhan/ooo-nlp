"""Sample file to run spacy for Global OIC"""

__author__ = 'Anuj Chauhan'

import spacy
import sys
import json

sample_text = u"""Hi,

I'm in training till January 14.

For MarkitWire related queries contact Archit Kapoor.
For iLab related queries contact Aravind Rao.

For any escalations contact my manager Sunil Vishwa Shingate.

Thanks and Regards,
Anuj Chauhan
"""

USEFUL_TAGS = [u'NN', u'NNS']
USEFUL_VALS = [u'NNP', u'NNPS']

EN_NLP = None

def init_spacy():
	global EN_NLP
	EN_NLP = spacy.load('en')
	return EN_NLP

def get_sentences(text):
	return text.split('.')

def perform_nlp(text):
	en_doc = EN_NLP(text)
	
	tags = [word.text for word in en_doc if word.tag_ in USEFUL_TAGS]
	vals = [word.text for word in en_doc if word.tag_ in USEFUL_VALS]
	return {
		' '.join(tags): ' '.join(vals)
	}

def doit():

	sentences = get_sentences(sample_text)
	final_json = dict()
	for sentence in sentences:
		tokens = perform_nlp(sentence)
		final_json.update(tokens)
		# for word in tokens:
		# 	sys.stdout.write(str([word.text, word.lemma, word.lemma_, word.tag, word.tag_, word.pos, word.pos_]) + '------')
		# print ''
	print json.dumps(final_json, indent=4)

if __name__ == '__main__':
	init_spacy()
	doit()
