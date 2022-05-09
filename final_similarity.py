# install nltk library and stopwords list first
# nltk.download('stopwords')  #or 
# python -m nltk.downloader stopwords
# __Masoom Group__

from collections import Counter
import math
import string
import sys
import nltk

stop_words = nltk.corpus.stopwords.words('english')

# +string(stop_words)

def read_file(filename):	
	try:
		with open(filename, 'r') as f:
			data = f.read()
		return data	
	except IOError:
		print("Error in opening or reading input file: ", filename)
		sys.exit()

def rm_punct(data):
	translation_table = data.maketrans(string.punctuation+string.ascii_uppercase,
									" "*len(string.punctuation)+string.ascii_lowercase)
	data = data.translate(translation_table)
	data = data.split()	 
	return data

def rm_stopwords(data):
	l = []
	for i in data:
		if i not in stop_words:
			l.append(i)
	return l

def rm_repwords(data):
	l = []
	for i in data:
		if i not in l:
			l.append(i)
	return l 

def text_cleaner(file):
	data = read_file(file)
	data = rm_punct(data)
	data = rm_repwords(data)
	data = rm_stopwords(data)
	return data


def check_similarity(data1, data2):
	l = []
	for i in data1:
		for j in data2:
			if i == j and i  not in l:
				l.append(i)

	# print( "list of similar words = ",l, " \n" )
	data = data1 + data2
	print("The most occuring words", Counter(data).most_common(4))	
	data = rm_repwords(data)
	sm = math.trunc(((len(l)/len(data))*100))

	return sm


def check(file1, file2):
	data1 = text_cleaner(file1)
	data2 = text_cleaner(file2)
	data = check_similarity(data1, data2)
	
	print('\nSimilarity btw the Documents is: ', data, "%  <---")



# Start From here  |
#                  v

check("doc1.sa", "doc2.sa")


