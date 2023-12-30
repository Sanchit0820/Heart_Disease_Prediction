# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OC67Wlq9FNK1ENQMgKZO-CNV7lz5l6rq
"""

!pip install pandas
!pip install numpy
!pip install seaborn
!pip install matplot
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
df= pd.read_csv(r'/content/heart.csv')
df.head()

df.rename(columns={'age':'Age', 'sex': 'Sex','cp': 'Chest_pain', 'trestbps' : 'Resting_blood_pressure','chol': 'Cholestrol', 'fbs':'Fasting_blood_sugar', 'thalach': 'Maximum_heart_rate', 'exang':'Exercise_induced_angina','oldpeak': 'ST_depression', 'slope': 'ST_slope', 'ca' : 'Major_ vessels','thal' : 'Thalessemia_types', 'target' : 'Heart_disease'}, inplace=True)
print(df.head())

plt.figure(figsize=(10,6))
#Target is equal to 1
plt.scatter(x= df[df['Heart_disease'] ==1]['Age'], y= df.Maximum_heart_rate[df.Heart_disease==1])

#Target is equal to 0
plt.scatter(x= df[df['Heart_disease']==0]('Age'), y = df.Maximum_heart_rate[df.Heart_disease==0],);

#Adding some helpful information
plt.title("Heart disease in function of Age and Max Heart rate Rate")
plt.xlabel("Age")
plt.ylabel("Max.Heart Rate")
plt.legend(["Disease", "No disease"])



pd.crosstab(df['Chest_pan'],df['Heart_disease'])

pd.crosstab(df['Chest_pan'], df[ 'Heart_disease']). plot (kind='bar')
plt.title("Heart Disease Frequency per Chest Pain Type")
plt.xlabel("Chest Pain types")
plt.ylabel("Amount")
plt.legend(['No disease', 'Disease'])
plt.xticks(rotation=0);

df['Resting_blood_pressure'].plot(kind='kde')

sns.catplot(x="ST_slope", y="Cholestrol", hue="Sex", kind="boxen", data=df)
plt.xlabel('slope (slope of heart rate)')
plt.ylabel('cholestrol')
plt.title(label="Relation Between heart rate slope and cholestrol level with respect to gender", loc ='center')

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

sns.set(font_scale=1.5)
def plot_confusion_matrix(y_test, y_preds)
fig,ax=plt.subplots(figsize=(3,3))
ax=sns.heatmap(confusion_matrix(y_test,y_preds), annot=True,cbar=False)
plt.xlabel("True Label")
plt.ylabel("Predicted Label")
plot_conf_mat(y_test, lr_y_preds)