#K-Means Elbow Method

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load and Prepare Data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Step 2: Standardize the Data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# Step 3: Apply KMeans with Different Values of K and Record Inertia - sum of squared distances from points to their cluster centers
inertia = []
k_range = range(1, 11)  # Trying K from 1 to 10

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

# Step 4: Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o', linestyle='-', color='teal')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.xticks(k_range)
plt.grid(True)
plt.show()

#Step 5 : the Model
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Train final KMeans model
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
cluster_labels = kmeans.fit_predict(df_scaled)

#Step 6: Visualize
# Reduce dimensions for visualization
pca = PCA(n_components=2)
pca_data = pca.fit_transform(df_scaled)

# Plot clusters
plt.figure(figsize=(8, 5))
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=cluster_labels, cmap='viridis', s=50)
plt.title('KMeans Clustering Visualization (PCA-Reduced)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.grid(True)
plt.show()
