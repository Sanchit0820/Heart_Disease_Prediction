# Importing the dependencies
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Data Collection and Processing
# loading the csv data to a pandas dataframe
heart_data = pd.read_csv(r'C:\Users\sanch\OneDrive\Documents\heart.csv')

# print first 5 rows of the dataset
heart_data.head()
print(heart_data.head())

#print last 5 rows of the datset
heart_data.tail()
print(heart_data.tail())

# number of rows and columns in the dataset
heart_data.shape
print(heart_data.shape)

#getting some info about the data
heart_data.info()
print(heart_data.info())

# checking for missing values
heart_data.isnull()
print(heart_data.isnull())

# statistical measures of the data
heart_data.describe()
print(heart_data.describe())

# checking the distribution of target variable
heart_data['target'].value_counts()
print(heart_data['target'].value_counts())

# 1 - DEFECTIVE HEART
# 0 - HEALTHY HEART

# Splitting the Features and Target
X = heart_data.drop(columns= 'target', axis=1)
Y = heart_data['target']
print(X)
print(Y)

# Splitting the data into Training Data and Test Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)

#   Model Training
LogisticRegression
model = LogisticRegression()
# training the LogisticRegression model with Training Data
model.fit(X_train, Y_train)

# Model Evaluation
#Accuracy Score
# accuracy on Training Data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on Training Data :', training_data_accuracy)

# accuracy on Testing Data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test Data :', test_data_accuracy)

# Building a predictive system
input_data = (70,1,0,145,174,0,1,125,1,2.6,0,0,3)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
    print("The person does not have a heart disease")
else:
    print("The person has heart disease")

