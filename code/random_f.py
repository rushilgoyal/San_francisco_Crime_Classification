


import numpy as np
import pandas as pd
import scipy as sp
from patsy import dmatrices, dmatrix
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, log_loss
from sklearn.decomposition import IncrementalPCA

class Predictions():
	df_train = 0
	df_test = 0
	def __init__(self):
		self.df_train = pd.read_csv("/Users/rushilgoyal/Desktop/train2.csv", parse_dates=["Dates"])
		self.df_test = pd.read_csv('/Users/rushilgoyal/Desktop/test2.csv', parse_dates=['Dates'])


	def Random(self):

		print "number of crime_incidents", len(self.df_train)
		# Dropping Description and Resolution variables since they are not there in test dataset
		self.df_train.drop(['Descript', 'Resolution'], axis=1, inplace=True)
		print "This is how the training crime data looks "
		print self.df_train.head(3)
		

		# Vectorising Date variable by extracting fetaures for hours, months and years.
		# Also extracting binary features for district and day_of_week
		hours = pd.get_dummies(self.df_train.Dates.map(lambda x: pd.to_datetime(x).hour), prefix="hour")
		months = pd.get_dummies(self.df_train.Dates.map(lambda x: pd.to_datetime(x).month), prefix="month")
		years = pd.get_dummies(self.df_train.Dates.map(lambda x: pd.to_datetime(x).year), prefix="year")
		district = pd.get_dummies(self.df_train["PdDistrict"])
		day_of_week = pd.get_dummies(self.df_train["DayOfWeek"])

		
		# Concatenating these vectorized variables to generate training dataset
		X_training = pd.concat([self.df_train, hours, months, years, district, day_of_week], axis=1)
		# Dropping "Address" since its already represented by Latitude and Longitude
		# Dropping "Dates", "DayOfWeek" and "PdDistrict" since they have already been vectorized into additional features
		X_training = X_training.drop(["Dates", "Address", "DayOfWeek", "PdDistrict"],  axis = 1)
		print "The new training dataset looks something like this"
		X_training.head(2)


		# Generating training and validation index for splitting the training data
		inds = np.arange(X_training.shape[0]) 
		# Shuffling the indexes
		np.random.shuffle(inds)
		# Taking 70% of the shuffled data
		train_inds = inds[:int(0.7 * X_training.shape[0])]
		# Remaining 30% for the validation purpose
		val_inds = inds[int(0.7 * X_training.shape[0]):]

		# Generating validation and training datasets based on indexes
		df_val = X_training.ix[val_inds]
		df_train = X_training.ix[train_inds]
		
		# Extracting the Crime category as the training output
		y_tr = df_train["Category"]
		# Ridding it out from the input features
		X_tr = df_train.drop("Category", axis = 1)
		# Repeating the same for validation dataset
		y_val = df_val["Category"]
		X_val = df_val.drop("Category", axis = 1)

		print "Lets try Random Forest"
		print "Fitting Random Forest classifier..." 
		# Invoking random forest classifier
		rf_clf = RandomForestClassifier(n_estimators=10)

		# Fitting random forest classifier
		rf_clf.fit(X_tr, y_tr.ravel())
		rf_classifier = rf_clf.fit(X_tr, y_tr.ravel())

		print "Calculating Accuracy for  random forest model"
		print 'Mean accuracy (rf_clf): {:.4f}'.format(rf_clf.score(X_val, y_val.ravel()))

		# Pre-processing the test dataset
		hours = pd.get_dummies(self.df_test.Dates.map(lambda x: pd.to_datetime(x).hour), prefix="hour")
		months = pd.get_dummies(self.df_test.Dates.map(lambda x: pd.to_datetime(x).month), prefix="month")
		years = pd.get_dummies(self.df_test.Dates.map(lambda x: pd.to_datetime(x).year), prefix="year")
		district = pd.get_dummies(self.df_test["PdDistrict"])
		day_of_week = pd.get_dummies(self.df_test["DayOfWeek"])


		X_test = pd.concat([self.df_test, hours, months, years, district, day_of_week], axis=1)
		X_test = X_test.drop(["Id", "Dates", "Address", "DayOfWeek", "PdDistrict"],  axis = 1)

		# Fitting the classifer
		output = rf_classifier.predict(X_test)

		return output






