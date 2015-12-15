from sklearn import preprocessing
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
class Adaboost:
	def __init__(self, n=200, rate=0.1):
		self.le = preprocessing.LabelEncoder()
		self.model = AdaBoostClassifier(n_estimators = n, learning_rate = rate)

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

