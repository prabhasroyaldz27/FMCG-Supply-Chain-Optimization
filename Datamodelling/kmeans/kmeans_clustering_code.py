import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("FMCG_data.csv")

# Select features
X = data[['zone', 'Location_type', 'num_refill_req_l3m']]
X = pd.get_dummies(X, columns=['zone', 'Location_type'], drop_first=True)

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Apply KMeans with 3 clusters
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
data['Demand_Cluster'] = kmeans.fit_predict(X_scaled)

# Silhouette score
sil_score = silhouette_score(X_scaled, data['Demand_Cluster'])
print("Silhouette Score for K-Means Clustering:", sil_score)

# Plot clusters
sns.scatterplot(x='zone', y='num_refill_req_l3m',
                hue='Demand_Cluster', data=data, palette='viridis')
plt.title('Regional Demand Clusters')
plt.show()
