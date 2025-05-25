#Boosting Algorithm: AdaBoost

#Step 1: Load necessary libraries
import pandas as pd

# Step 2: Load the Dataset
from sklearn import datasets
iris = datasets.load_iris()

#Convert to DataFrame
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df.head()

#Step 3: Prepare x & y 
x = iris.data
y = iris.target

#Step 4: Split the Training & Testing Data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.7, random_state=42 )

#Step 5: Build the Model
from sklearn.ensemble import AdaBoostClassifier
#Create instance
clf = AdaBoostClassifier(n_estimators=100, learning_rate=1.0, random_state=45)
#Train the Model
model = clf.fit(x_train,y_train)

#Step 6: Test the Model
y_pred = model.predict(x_test)

#Step 7: Evaluate the Model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
print('Accuracy Score : ', accuracy_score(y_test,y_pred)*100, ' %')
print("\nConfusion Matrix : \n", confusion_matrix(y_test,y_pred))
print("\nClassification Report : \n", classification_report(y_test,y_pred))
