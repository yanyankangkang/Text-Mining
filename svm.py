from sklearn import preprocessing
from sklearn import metrics
from sklearn import svm
class SupportVectorMachine:
	def __init__(self, p='l1', c=1):
		self.le = preprocessing.LabelEncoder()
		self.model = svm.LinearSVC(class_weight = 'auto', penalty=p, C = c, dual=False)
	def train(self, X, y):
		self.le.fit(y)
		y = self.le.transform(y)
		self.model.fit(X, y)

	def predict(self, X):
		pred = self.model.predict(X)
		pred = self.le.inverse_transform(pred)	
		return pred

	def evaluate(self, X, y):
		y = self.le.transform(y)
		pred = self.model.predict(X)
		return metrics.f1_score(y, pred, average='macro')