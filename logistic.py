#Logistic Regression

#Step 1: Import Necessary Libraries
import pandas as pd
import numpy as np

#Step 2: Load the Dataset
data = pd.read_csv("/content/diabetes.csv")
print(data.head())

#Step 3: PreProcessing teh data
#Stastical summary of Data
data.describe()
#Visualization
#Draw a Scatter plot for Glucose & Diabetes
import seaborn as sns
sns.scatterplot(data=data, x='Glucose', y='Outcome', color='red')

#Find value counts of Outcome
data.Outcome.value_counts()

#Draw a Barplot
data.Outcome.value_counts().plot(kind='bar',x='Outcome (0 = No Diabetes, 1 = Diabetes)',y='Count', color='pink')

#Step 4: Prepare x & y
features =['Pregnancies',  'Glucose',  'BloodPressure',  'SkinThickness',  'Insulin',  'BMI', 'DiabetesPedigreeFunction', 'Age']
x = data[features]
y = data.Outcome

#Step 5 : Split the dataset in Training & Testing Dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,train_size=0.8,random_state=100)
x_train.shape #Show the no of rows and cols

#Step 6: Build & Train the Model
from sklearn.linear_model import LogisticRegression

#Creating an Instance
logr = LogisticRegression(max_iter=100)

#Training the model
logr.fit(x_train,y_train)

#Step 7: Test the Model
y_pred = logr.predict(x_test)

#Step 8: Measure the Performance of the Model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#Accuracy
print("Accuracy Score : ", accuracy_score(y_test,y_pred))

#Confusion Matrix
print("Confusion Matrix : \n", confusion_matrix(y_test,y_pred))

#Classification Report
print("Classification Report : \n", classification_report(y_test,y_pred))
