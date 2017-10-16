
# This is a test for Random Forests

import pandas as pd

from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv('/Users/rushilgoyal/Desktop/train.csv')
# Labelling it as training dataset
X_tr = data

# Extracting the Category (Output Varible) of the Crime Dataset into another dataframe for prediction
y_tr = data["Category"]

# Ridding the category variable from the input set of training data
X_tr = X_tr.drop("Category", axis=1)


# To maintain consistency with the test set, we are ridding of the Descript and Resolution Variable
# Also given the fact that considering 'Descript' variable will have a bias in prediction accuracy since 
# it already implies information about the category of the crime which we intend to predict otherwise
X_tr = X_tr.drop("Descript", axis=1) 
X_tr = X_tr.drop("Resolution", axis=1)



# build categorical features
hours = pd.get_dummies(X_tr.Dates.map(lambda x: pd.to_datetime(x).hour), prefix="hour")
months = pd.get_dummies(X_tr.Dates.map(lambda x: pd.to_datetime(x).month), prefix="month")
years = pd.get_dummies(X_tr.Dates.map(lambda x: pd.to_datetime(x).year), prefix="year")
district = pd.get_dummies(X_tr["PdDistrict"])
day_of_week = pd.get_dummies(X_tr["DayOfWeek"])
 


# string them all together
X_training = pd.concat([X_tr, months, years, district, day_of_week], axis=1)

   
# Removing the original time stamp
X_training.drop(['Dates', 'Address','DayOfWeek', 'PdDistrict'], axis=1, inplace=True) 

    

# loading test data
data = pd.read_csv('/Users/rushilgoyal/Desktop/test.csv', index_col="Id")
X_test = data

#print(X_test.head(3))
    
# PROCESSING TEST DATASET   
 
# build categorical features
hours = pd.get_dummies(X_test.Dates.map(lambda x: pd.to_datetime(x).hour), prefix="hour")
months = pd.get_dummies(X_test.Dates.map(lambda x: pd.to_datetime(x).month), prefix="month")
years = pd.get_dummies(X_test.Dates.map(lambda x: pd.to_datetime(x).year), prefix="year")
district = pd.get_dummies(X_test["PdDistrict"])
day_of_week = pd.get_dummies(X_test["DayOfWeek"])
    
# string them all together
test_X = pd.concat([X_test, hours, months, years, district, day_of_week], axis=1)
test_X.drop(['Dates', 'Address','DayOfWeek', 'PdDistrict'], axis=1, inplace=True) 


#print("Test Data")
#print(Test_X.head(4))

# FITTING RANDOM FORST CLASSIFIER    
print("Fitting classifier...")   
clf = RandomForestClassifier(n_estimators=10)
# TRAINING THE DATASET
clf.fit(X_training, y_tr)
print('Predicting...')
output = pd.DataFrame(clf.predict_proba(test_X), index=test_X.index, columns=clf.classes_)

#output = forest.predict.predict_proba(test_X)
    

output = ["%f" % x[1] for x in output]
output.to_csv("results.csv", index_label="Id")
#csv_io.write_delimited_file('/Users/rushilgoyal/Desktop/rf.csv', output)
# print(output.head(5))

# y_test = pd.DataFrame(clf.predict_proba(X_test), index=X_test.index, columns=clf.classes_)
    
#y_test.to_csv("results.csv", index_label="Id")  '''  
    
