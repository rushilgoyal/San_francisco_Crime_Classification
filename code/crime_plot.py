
# coding: utf-8

# In[2]:

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn import cross_validation
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from patsy import dmatrices, dmatrix



class Crime_Stats():
	def __init__(self):
		self.train_df = pd.read_csv("/Users/rushilgoyal/Desktop/train2.csv", parse_dates=["Dates"])
	

	def visualisation(self):
		get_ipython().magic(u'matplotlib inline')
		self.train_df.Category.value_counts().plot(kind="bar")
        # Parsing the dates
		self.train_df["Hour"] = self.train_df["Dates"].map(lambda x: x.hour)
		#The following three visualisations give us an idea of the number of crimes by Day, District and by Hour
		#1.  PLOTTING THE COUNT OF CRIME BY HOUR
		self.train_df["event"] = 1
		hourly_event = self.train_df[["Hour", "event"]].groupby(["Hour"]).count().reset_index()
		hourly_event.plot(kind="bar")
		plt.show()


		#2.  PLOTTING THE COUNT OF CRIME BY DISTRICT
		dist_count = self.train_df.PdDistrict.value_counts()
		plt.figure()
		dist_count.plot(kind="barh")
		plt.ticklabel_format(style='plain', axis='x', scilimits=(0, 0))
		plt.tight_layout()
		plt.show()


		#3.  PLOTTING THE COUNT OF DAY OF WEEK
		day_count = self.train_df.DayOfWeek.value_counts()
		plt.figure()
		day_count.plot(kind="barh")
		plt.ticklabel_format(style='plain', axis='x', scilimits=(0, 0))
		plt.tight_layout()
		plt.show()






