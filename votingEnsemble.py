#Boosting Algorithm: Voting Ensemble

#Step 1: Import necessary libraries
import pandas as pd

#Step 2: Load the Dataset
from sklearn import datasets
iris = datasets.load_iris()
#Convert to DF
iris_df = pd.DataFrame(iris.data,columns =iris.feature_names)

#Step 3: Prepare x & y
x = iris.data
y = iris.target

#Step 4: Split the training & testing data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.7, random_state=42 )

#Step 5: Build the Models
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

# Create base models
log_clf = LogisticRegression(max_iter=1000, random_state=42)
tree_clf = DecisionTreeClassifier(random_state=42)
svm_clf = SVC(probability=True, random_state=42)

# Combine models in a voting classifier
voting_clf = VotingClassifier(estimators=[
    ('lr', log_clf), 
    ('dt', tree_clf), 
    ('svm', svm_clf)],
    voting='soft'  # or 'hard'
)

# Step 6: Train
voting_clf.fit(x_train, y_train)

# Step 7: Predict
vote_pred = voting_clf.predict(x_test)

#Step 8: Evaluate
print("=== Voting Classifier Results ===")
print("Accuracy:", accuracy_score(y_test, vote_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, vote_pred)*100," %")
print("Classification Report:\n", classification_report(y_test, vote_pred))
