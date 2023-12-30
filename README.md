INTRODUCTION:

Cardiovascular disease is among the world's most lethal conditions (CVD). Global
Burden of Disease (GBD) studies and the World Health Organization (WHO) have
ranked cardiovascular disease as the top cause of mortality globally each year [40, 56].
According to the WHO, more than 23.6 million people are expected to be affected by
CVD by the year 2030. Several industrialised countries, including the United States of
America, experience about 1 in 4 deaths [34]. The Middle East and North Africa
(MENA) region has an even higher mortality rate, at 39.2% [20]. Therefore, the key to
reducing the number of cardiovascular diseases that cause death is the provision of
appropriate treatments and early, accurate diagnosis. Medical diagnosis is seen as a
necessary but challenging duty that must be completed successfully and rapidly. This
task's automation is quite beneficial. In order to successfully predict the presence of heart
diseases we have chosen 14 different variables which will assist us in the task of
diagnosing heart diseases.


There are 14 columns in the data set which are set out as mentioned below :


1.Age: It is a continuous data type that indicates a person's age in years.

2.Sex: is a discrete data type that identifies a person's gender. Here, 0 denotes a woman and
1 a man.

3.CP (chest pain type) : It is a discrete data type that categorizes different types of chest
pain into the following categories: typical angina, atypical angina, non-anginal pain, and
asymptotic angina.

4.Trestbps: The resting blood pressure is expressed as a continuous data type in mm Hg.

5.Cholesterol: The milligrammes per deciliter value for serum cholesterol is specified in a
continuous data format.

6.FBS: It compares a person's fasting blood sugar level to 120 mg/dl and is a discrete data
type. FBS >120 causes 1 to be true and 0 to be false.

7.RestECG: It is a discrete data format that displays the results of the resting ECG, with 0
denoting normality, 1 denoting an ST-T wave irregularity, and 2 denoting left ventricular
hypertrophy.

8.Thalach: The maximum heart rate attained is described via a continuous data type.
Exang: Exercise-induced angina is indicated by the discrete data type 1 = Yes and 0 =
No.

9.Oldpeak: It displays the depression brought on by exercise in relation to weight and is a
continuous data type.

10.Slope: It is a discrete data type that depicts the slope of the peak workout segment, with 1
denoting an upward slope, 2 a flat gradient, and 3 a downward gradient.

11.Ca: It is a continuous data format that displays a range of 0 to 3 main vessels that have
been fluoroscopically coloured.

12.Thal: Thalassemia is displayed using a discrete data type, with 3 denoting normal, 6
denoting a fixed defect, and 7 denoting a reversible defect.

13.Class: It is a discrete data type, with diagnosis class 0 denoting No Presence and range
1–4 denoting the likelihood that the subject has a cardiac condition, with 1 denoting the
least likelihood.

14.Target Variable: In essence, a target variable is one whose values are predicted and
modeled by other variables. In this case, our target variable or the dependent variable is Y
on the basis of which we have continued the testing and training of our model. The target
variable can have values of 1 or 0


RESEARCH METHODOLOGY:

The main purpose of the proposed method is to predict the occurrence of heart disease for
early detection of the disease in a short time. In our approach, we are using different
machine learning algorithms. Naïve Bayes, k Nearest Neighbour (KNN), Random Forest
to predict heart disease based on some health parameters.
First step is to get the data set and then processing of the data set is done as we can not
use the raw data so we need to process this data and convert it into a compatible machine
learning algorithm. After processing, we need to split the data into training data and
testing data. And then we will evaluate our model using the test data . This part is called
the strain test split. Then we feed our training data to our machine learning model. In this
step we used a logistic regression model. As this case is binary classification as we are
classifying if a person has a deceased art or not .On training this logistic regression
model with our training data we did some evaluation to check its performance. We
trained a logistic model and to this model we fed new data.
Data is analyzed using Pycharm editor community edition Notebook. It is an open source
software where we can implement multiple machine learning algorithms by importing
libraries.We downloaded libraries by installing through Pycharm settings. Data Analysis
is although is done on Google Collaboratory.
Developed by JetBrains as an IDE for Python application development, Pycharm is a
hybrid platform. It has modules and packages that make it easier and faster for
programmers to create Python-based software.



RESULT AND CONCLUSION:

The concept of many strategies that have been researched for diagnosing heart disease is
presented in this paper through a review of the literature while utilizing raw data.
For the most accurate analysis of the prediction model, machine learning can produce
promising results. The primary goal of this study is to diagnose cardiovascular disease or
heart disease utilizing a variety of techniques and procedures to obtain a prognosis.
As a measurement of our evaluation, we employed "accuracy score." With the help of
this, the target value will be anticipated by the model, and the forecast value will be
compared to the initial target values. This is done initially on the practise data, and the
value is saved in the variable training data accuracy. The accuracy rating for training data
is 85%. For test data, we additionally require an accuracy score. Finding the X-test target
and comparing the projected values to the Y-test are the next steps. The test data accuracy
comes out to 82%. If the accuracy score between the training and test sets is not nearly
identical, overfitting will become an issue.
