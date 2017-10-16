# San_francisco_Crime_Classification

The following files are contained in this project:

#Codes
a. Consolidated code
b. Crime_plot
c. Random_f
d. Heatmap

# Modeling codes
A brief description of each modeling code:

Random Forsest.py - 
1. In this code, i use the getdummy() function to encode some input categorical features into binary matrices because a lot of algorithms do not work well with 'string' representation. The algorithm that I used here is Random Forest

Naive Bayes.py - 
2. In the second code, I am basically converting the given categorical into numericals (example: Monday: 1, Tuesday: 2, Wednesday: 3 and so on.) I do this process similarly for Crime Category, PdDistrict. I didn't include the Address variable since X(latitude) and Y(longitude) already incorporates information about the address. The algorithm used is Logistic Regression. I also created some plots (also attached)

log.py
3. The third code is slightly complicated given the fact that I included Address along with the numerical representations of other categorical variables (same as second, but I also include the Address variable here). Since the Address variable is basically a string, I apply countvectorizer() function to create bag-of-word features (basically a frequency representation of all the unique words in the dataset). The algorithm I use here is Logistic Regression. 




#Data files: 
a.Demographics.csv
b. Police.csv
c.Train2.csv
d.Test2.csv

#Performance evaluation file

It shows model performance evaluation for following comparisons across 3 different algorithms. (RandomForest, NaiveaBayes, Logistic)
a.Label Encoding
b. Vectorization of features
c. Word Vectorization of address
