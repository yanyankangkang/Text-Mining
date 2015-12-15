from sklearn import preprocessing
from sklearn import datasets
from adaboost import Adaboost
from logistic import Logistic
from svm import SupportVectorMachine
from scipy import sparse
import feature_tag
import feature_hy
import numpy as np
import pickle
import os
import sys
def blackbox(type, X, y):
	''' return training error, if the method is not found, return None
	'''
	clf = None
	if type == 'adaboost':
		clf = Adaboost()
	elif type == 'logistic':
		clf = Logistic()
	elif type == 'svm':
		clf = SupportVectorMachine()
	else:
		return None
	clf.train(X, y)
	pickle.dump(clf, open(type, 'w'))
	return (clf.evaluate(X, y), clf)


def getData(filename, type):
	yan_size = 137316
	rows = 46435
	if type == 'train':
		rows =203621
	X = sparse.lil_matrix((rows, yan_size+12))
	y = []
	if not os.path.exists(filename + 'hao'):
		feature_tag.process_file(filename, filename+'hao')
		feature_hy.getData(filename, filename+'yan', type)
	with open(filename+'yan', 'r') as reader:
		for line in reader:
			if line == '\n':
				break
			parts = line.strip('\n').split(',')
			y.append(parts[0])
			row = len(y)-1
			for i in range(1, len(parts)):
				X[row, int(parts[i])] = 1
	with open(filename+'hao', 'r') as reader:
		row = 0
		for line in reader:
			if line == '\n':
				break;
			parts = line.strip('\n').split(',')
			for i in range(0, len(parts)):
				X[row, yan_size+int(parts[i])-1] = 1
			row += 1
		X = sparse.csr_matrix(X)
	return X,y

def getSentence(line):
	X1 = feature_hy.processSentence(line)
	X2 = feature_tag.process_sentence(line)
	yan_size = 137316
	X = sparse.lil_matrix((len(X1), yan_size+12))
	for wordX1, wordX2 in zip(X1,X2):
		row = 0
		for x in wordX1:
			X[row, x] = 1
		row += 1
		row = 0
		for x in wordX2:
			X[row, x] = 1
		row += 1
	X = sparse.csr_matrix(X)
	return X

if __name__ == '__main__':
	# vocabulary = pickle.load(open('vocabulary', 'r'))
 #    vocabularyStem = pickle.load(open('vocabularyStem', 'r'))
 #    vocabularyPrev = pickle.load(open('vocabularyPrev', 'r'))
 #    vocabularySuff = pickle.load(open('vocabularySuff', 'r'))
 	
 	clf = None
 	if not os.path.exists('model'):
		X,y = getData('eng.train.txt', 'train')
		print 'train loaded ...'
		(train_score, clf) = blackbox('svm', X, y)
		pickle.dump(clf, open('model', 'w'))
		print 'model trained ...'
		X,y = getData('eng.test.txt', 'test')
		print 'test loaded ...'
		test_score = clf.evaluate(X, y)
		print test_score
	else:
		clf = pickle.load(open('model', 'r'))
	

	while 1:
		line = raw_input()
		if line == 'end':
			break
		X = getSentence(line)
		print line
		pred = clf.predict(X)
		print pred
		
	
