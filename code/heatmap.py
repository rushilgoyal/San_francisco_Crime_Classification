
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


class heatmap():

	def __init__(self):
		self.sf_df = pd.read_csv('/Users/rushilgoyal/Desktop/train2.csv')   #load the dataset


	def crime_heatmap(self):

		#self.sf_df.info()
		#self.sf_df.columns#columns used
		#self.sf_df.head(5)
		self.sf_df.PdDistrict.value_counts().plot(kind="bar")

		self.sf_df_crosstab = pd.crosstab(self.sf_df.PdDistrict,self.sf_df.Category,margins=True)
		del self.sf_df_crosstab['All']#delete All column
		self.sf_df_crosstab = self.sf_df_crosstab.ix[:-1]#delete last row (All)

       #  PLOTTING HEATMAP OF CRIME INCIDENTS BY Police District
		column_labels = list(self.sf_df_crosstab.columns.values)
		row_labels = self.sf_df_crosstab.index.values.tolist()

		fig,ax = plt.subplots()
		heatmap = ax.pcolor(self.sf_df_crosstab,cmap=plt.cm.Blues)




