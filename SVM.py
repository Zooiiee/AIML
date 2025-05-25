#Support Vector Machine (SVM)

#Step 1: Load the Dataset
from sklearn import datasets
cancer = datasets.load_breast_cancer()

#Step 2: Prepare x & y
x = cancer.data
y = cancer.target

#Step 3: Split Training and Testing Data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x,y, test_size=0.8, random_state=45)

#Step 4: Build the model
from sklearn import svm
#Create instance
svm_clf = svm.SVC(kernel='linear')

#Step 5: Train the Model
model = svm_clf.fit(x_train,y_train)

#Step 6: Test the Model
y_pred = model.predict(x_test)

#Step 7: Evaluate the Model
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
print("=== SVM ===")
print("Accuracy:", accuracy_score(y_test, y_pred)*100," %")
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

