#Bagging Algorithm: Random Forest 

# Step 1: Import necessary libraries
import numpy as np
import pandas as pd

#Step 2 : Load Dataset
banking = pd.read_csv("/content/banking.csv")
banking.head()
banking.info()

#Step 3: Define Traget Attribute
#Target Attribute : y - Person opts for term deposit : yes or no
banking.y.value_counts()

banking.default.unique()
banking.default.value_counts()
banking['default'] = banking['default'].map({'no':0, 'unknown':0, 'yes':1})
banking.default.value_counts()

#Step 4: Define Important Features
features = ['age','default','cons_conf_idx','emp_var_rate']

#Step 5: Prepare x & y
x = banking[features]
y = banking.y

#Step 6 : Split the training and Testing data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y,train_size=0.8, random_state=45)

#Step 7: Create and Train the Random Forest Model
from sklearn.ensemble import RandomForestClassifier
# Create the Random Forest model (Bagging)
rf_model = RandomForestClassifier(n_estimators=1000, criterion='entropy', max_depth=5, bootstrap=True, random_state=45)  # 1000 trees in the forest
#Train the Model
rf_model.fit(x_train,y_train)

#Step 8: Make Predictions
y_pred = rf_model.predict(x_test)

#Step 9: Evaluate the Model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
print("Accuracy Score : ", accuracy_score(y_test,y_pred)*100, " %")
print("\nConfusion Matrix : \n", confusion_matrix(y_test,y_pred))
print("\nClassification Report : \n", classification_report(y_test,y_pred))

#Step 10: HyperParameter Tuning
from sklearn.model_selection import GridSearchCV
param_grid = {
    'n_estimators':[100,500,100],
    'criterion':['entropy','gini'],
    'max_depth':[None,5,10],
    'max_features':['auto','sqrt','log2'],
    'bootstrap':[True,False]
}

rfc = RandomForestClassifier(random_state=45)
#Perform GridSearch
grid_search = GridSearchCV(estimator=rfc, param_grid=param_grid, n_jobs=1, scoring='accuracy')
#Train
grid_search.fit(x_train, y_train)
best_param = grid_search.best_params_
best_score = grid_search.best_score_

print('Best Parameters : ', best_param)
print('\nBest Score : ', best_score)
