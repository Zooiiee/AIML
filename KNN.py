#KNN

#Step 1: Load the Dataset
import pandas as pd

diab = pd.read_csv("/content/diabetes.csv")
diab.head()
diab.describe()

#Visualizations
#Plot Histogram
diab.hist(figsize=(20,20))

#Find counts of outcome
diab.Outcome.value_counts()
#Draw Outcome bar pot
diab.Outcome.value_counts().plot(kind='bar')

#Draw a Pairplot
import seaborn as sns
sns.pairplot(diab, hue="Outcome")

#Find Correlation coefficient
diab.corr()
#Visualize dorrelation
import matplotlib.pyplot as plt
plt.figure(figsize=(12,10))
sns.heatmap(diab.corr(),annot=True)

#Step 2: Prepare x & y
x= diab.drop("Outcome",axis=1)
y= diab.Outcome

# Step 3: Normalize / Standardize
from sklearn.preprocessing import StandardScaler
ss= StandardScaler()
x_transformed = pd.DataFrame(ss.fit_transform(x),columns=x.columns)
x_transformed.head()

#Step 4: Split the data into training & testing data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test= train_test_split(x_transformed,y,random_state=45)

# Step 5: Import KNN
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)

#Step 6: Test
y_pred =knn.predict(x_test)

#Step 7: Evaluate
from sklearn import metrics
print("=== KNN===")
print("Accuracy:", metrics.accuracy_score(y_test, y_pred)*100," %")
print("Confusion Matrix:\n", metrics.confusion_matrix(y_test, y_pred))
print("Classification Report:\n", metrics.classification_report(y_test, y_pred))

# run the model to find optimal value of k
train_scores = []

for i in range(1, 50):
    model = KNeighborsClassifier(i)
    model.fit(x_train, y_train)
    y_pred1 = model.predict(x_test)
    val = metrics.accuracy_score(y_test, y_pred1)
    train_scores.append(val)
    print("K=", i, ":", val)
