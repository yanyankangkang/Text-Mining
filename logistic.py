from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
class Logistic:
	def __init__(self, p='l1', c=1e5):
		self.le = preprocessing.LabelEncoder()
		self.model = LogisticRegression(penalty=p, C = c, class_weight = 'auto')

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