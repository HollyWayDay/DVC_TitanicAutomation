#@ Necessary libraries and dependencies
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette('cool')
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, f1_score, recall_score 

#@ Loading the csv file using pandas
df = pd.read_csv('titanic.csv') 

#@ Dropping passengerID as it has no significance for prediction
df.drop(['PassengerId'], axis=1, inplace=True)

#@ Dropping more unnecessary columns
df.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

#@ Filling null vlaues in Age column by the overall mean of that column
df['Age'].fillna((df['Age'].mean()), inplace=True) 
df = df.replace(np.nan, 'C', regex=True)
df = df.fillna('C') 

#@ Resolving categorical columns
gender = {'male': 1,'female': 2} 
embark = {'C': 0, 'Q': 1, 'S': 2}  
df.Sex = [gender[item] for item in df.Sex]  
df.Embarked = [embark[item] for item in df.Embarked] 

#@ Setting up variables for training
X = df.iloc[:, 1:8].values
y = df.iloc[:, 0].values 

# Splitting the dataset into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)  

# Feature Scaling
scaler_x = MinMaxScaler((-1,1))
X_train = scaler_x.fit_transform(X_train)
X_test = scaler_x.transform(X_test)  

#@ Making a list for storing the accuracy
accuracies = [] 

#@ Initializing the Logistic Regression Algorithm 
classifier = RandomForestClassifier(n_estimators=1700, criterion='gini')

#@ Fitting the classifier 
classifier.fit(X_train, y_train) 

#@ Prediction
y_pred = classifier.predict(X_test)

#@ Accuracy score
lr_score = classifier.score(X_test, y_test)

#@ Appending accuracy on accuracies list
accuracies.append(lr_score)

#@ Recall score
recall = recall_score(y_test, y_pred)

#@ f1 score
f1_score = f1_score(y_test, y_pred)

# Now print to JSON file
with open("metrics.json", 'w') as outfile:
        json.dump({ "accuracy": lr_score, "specificity": recall, "f1_score": f1_score }, outfile)

#@ Plotting the score figure
fig1_accu= sns.barplot(x=accuracies, y=['Models']) 

#@ Saving the plot in png format
plt.savefig("fig1_accu.png", dpi=120)  
