# Step 1: Load the dataset (Feature Extraction from structured dataset)
from sklearn import datasets
import pandas as pd
# Load Breast Cancer dataset
cancer = datasets.load_breast_cancer()
# Feature extraction: convert to DataFrame
cancer_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
print("Dataset Features :\n",cancer_df.head())

# View basic statistics of the features
print("Dataset Description:\n", cancer_df.describe())

# Step 2: Normalization / Standardization using Z-score
from sklearn.preprocessing import StandardScaler
# Standardize selected features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(cancer_df)
print("\nFirst Sample after Standardization:\n", X_scaled[0])

#Step 3: Find Principle Components
from sklearn.decomposition import PCA
# Reduce dimensionality to 2 components
pca = PCA(n_components=2)
#Fit the model 
x_pca = pca.fit_transform(cancer_df)
print("\nPCA Shape:", x_pca.shape)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)


# Step 2: Feature Selection
# Use statistical test (ANOVA F-test) to select top k features
from sklearn.feature_selection import SelectKBest, f_classif
# Select top 10 features based on F-score
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(cancer_df, cancer.target)
# Get names of selected features
selected_features = cancer_df.columns[selector.get_support()]
print("\nSelected Features:\n", selected_features.tolist())
