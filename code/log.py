# Adding the address variables adds a lot of complexity to the model. 
# In this model,  have tried to calcualte 

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




# Loading the training data
df_train = pd.read_csv('/Users/rushilgoyal/Desktop/train2.csv', parse_dates=['Dates'])
a = len(df_train)
# Getting rid of the Descript, Dates and Reslution variables
df_train.drop(['Descript', 'Dates', 'Resolution'], axis=1, inplace=True)
#print(df_train.head(3))

# Loading test dataset
df_test = pd.read_csv('/Users/rushilgoyal/Desktop/test2.csv', parse_dates=['Dates'])
df_test.drop(['Dates'], axis=1, inplace=True)
#print(df_test.head(3))

# Creating training and validation indexes for splitting the data
# shape is a tuple that gives dimensions of the array.
# np.arange() function builds a vector containing an arithmetic progression  
inds = np.arange(df_train.shape[0]) 


# Shuffling the indexes
np.random.shuffle(inds)

# Taking 70% of the shuffled data
train_inds = inds[:int(0.7 * df_train.shape[0])]


# Remaining 30% for the validation purpose
val_inds = inds[int(0.7 * df_train.shape[0]):]


#col_names = np.sort(df_train['Category'].unique())


# PRE-PROCESSING THE DATA

# Converting categorical variables into numerical variables in both train and test data
# Training Data
df_train['Category'] = pd.Categorical.from_array(df_train['Category']).codes
df_train['DayOfWeek'] = pd.Categorical.from_array(df_train['DayOfWeek']).codes
df_train['PdDistrict'] = pd.Categorical.from_array(df_train['PdDistrict']).codes

# Testing data
df_test['DayOfWeek'] = pd.Categorical.from_array(df_test['DayOfWeek']).codes
df_test['PdDistrict'] = pd.Categorical.from_array(df_test['PdDistrict']).codes



# Creating a features matrix of "Address" Variable
# Invoking the CountVectorizer library from sklearn
cvec = CountVectorizer(max_features = 300)


# Creating a word frequency matrix for Adrress Variable for training and testing  data
bows_train = cvec.fit_transform(df_train['Address'].values)
print(type(bows_train))
# Its a scipy matrix - 2-dimensional
bows_test = cvec.fit_transform(df_test['Address'].values)



# Splitting the data into training and validation sets using the indexes we created in the steps above
df_val = df_train.ix[val_inds]
print(type(df_val))
df_train = df_train.ix[train_inds]

# We use patsy‘s dmatrices function to create design matrices
y_train, X_train = dmatrices('Category ~ X + Y + DayOfWeek + PdDistrict', df_train)
# Horizontally stacking the Feature set of words frequency we obtained above
X_train = np.hstack((X_train, bows_train[train_inds, :].toarray()))
print(type(X_train))


# Repeating the same steps for Validation and Testing data set as well
y_val, X_val = dmatrices('Category ~ X + Y + DayOfWeek + PdDistrict', df_val)
X_val = np.hstack((X_val, bows_train[val_inds, :].toarray()))

X_test = dmatrix('X + Y + DayOfWeek + PdDistrict', df_test)
X_test = np.hstack((X_test, bows_test.toarray()))


# Fitting a Logistic Regression model
logistic = LogisticRegression()
logistic.fit(X_train, y_train.ravel())
classifier = logistic.fit(X_train, y_train.ravel())
print("Calculating Accuracy without PCA")
print('Mean accuracy (Logistic): {:.4f}'.format(logistic.score(X_val, y_val.ravel())))
predicted = classifier.predict(X_val)

#print(confusion_matrix(y_val, predicted))

   

#Use  PCA (Principal Component Analysis) to reduce the dimensionality
ipca = IncrementalPCA(n_components=4, batch_size=10)
X_train = ipca.fit_transform(X_train)
X_val = ipca.transform(X_val)
X_test = ipca.transform(X_test)

# Perorming the logistic regression again to see if the results improved
logistic_PCA = LogisticRegression()
logistic_PCA.fit(X_train, y_train.ravel())
classifier_PCA = logistic_PCA.fit(X_train, y_train.ravel())
Print("Accuracy with PCA")
print('Mean accuracy (Logistic): {:.4f}'.format(logistic_PCA.score(X_val, y_val.ravel())))



# Getting error in performing log loss 

#a = log_loss(y_val, predicted)
#print(a) '''





