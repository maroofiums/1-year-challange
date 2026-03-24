# Day357 - Mall Customer Segmentation

This project demonstrates customer segmentation using clustering techniques on a mall customer dataset. The goal is to identify distinct groups of customers based on **Age**, **Annual Income**, and **Spending Score** to support marketing and business decisions.

---

## Dataset

The dataset used is **Mall_Customers.csv**, which contains 200 customers with the following attributes:

| Column                 | Description                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
| CustomerID             | Unique ID of the customer                                                 |
| Gender                 | Male or Female                                                            |
| Age                    | Age of the customer                                                       |
| Annual Income (k$)     | Annual income in thousand dollars                                         |
| Spending Score (1-100) | Score assigned by the mall based on customer behavior and spending nature |

The dataset is clean with **no missing values**.

---

## Libraries Used

* `numpy` – numerical computations
* `pandas` – data manipulation
* `matplotlib` & `seaborn` – visualization
* `scikit-learn` – clustering algorithms (`KMeans`, `DBSCAN`, `AgglomerativeClustering`)
* `scipy` – hierarchical clustering visualization (`dendrogram`)
* `StandardScaler` – feature scaling

---

## Data Preprocessing

* Selected numerical features: **Age**, **Annual Income**, and **Spending Score**
* Standardized features using **StandardScaler** to ensure equal weight in clustering

---

## Clustering Techniques Implemented

### 1. K-Means Clustering

* Determined optimal clusters using **Elbow Method** (SSE vs. number of clusters)
* Best clusters identified: **6**
* Visualization: Customers grouped in 2D space (**Annual Income vs. Spending Score**)
* Summary of cluster centers:

| Cluster | Age   | Annual Income (k$) | Spending Score |
| ------- | ----- | ------------------ | -------------- |
| 0       | 56.33 | 54.27              | 49.07          |
| 1       | 32.69 | 86.54              | 82.13          |
| 2       | 25.56 | 26.48              | 76.24          |
| 3       | 26.13 | 59.42              | 44.45          |
| 4       | 44.00 | 90.13              | 17.93          |
| 5       | 45.52 | 26.29              | 19.38          |

---

### 2. Hierarchical Clustering

* Dendrogram created using **Ward linkage**
* Optimal clusters chosen: **5**
* Visualization: Customers clustered in 2D space (**Annual Income vs. Spending Score**)
* Summary of cluster centers:

| Cluster | Age   | Annual Income (k$) | Spending Score |
| ------- | ----- | ------------------ | -------------- |
| 0       | 26.56 | 47.36              | 56.79          |
| 1       | 56.40 | 55.29              | 48.36          |
| 2       | 32.69 | 86.54              | 82.13          |
| 3       | 43.89 | 91.29              | 16.68          |
| 4       | 44.32 | 25.77              | 20.27          |

---

### 3. DBSCAN

* Parameters: `eps=0.5`, `min_samples=5`
* DBSCAN identified **outliers** (`-1`) along with clusters 0–5
* Visualization: Customers plotted by **Annual Income vs. Spending Score**
* Summary of cluster centers:

| Cluster | Annual Income (k$) | Spending Score |
| ------- | ------------------ | -------------- |
| -1      | 68.53              | 31.53          |
| 0       | 25.82              | 78.18          |
| 1       | 27.80              | 31.80          |
| 2       | 54.16              | 48.41          |
| 3       | 54.32              | 50.46          |
| 4       | 80.88              | 83.63          |
| 5       | 78.71              | 14.57          |

---

## Insights

* **High-spending young customers** cluster separately from low-income or low-spending groups.
* **DBSCAN** is effective at detecting **outliers** that do not fit into any cluster.
* **K-Means** and **Hierarchical Clustering** show similar patterns but vary in cluster boundaries.

---

## Usage

1. Load the dataset:

```python
df = pd.read_csv("Mall_Customers.csv")
```

2. Scale features:

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_feature = scaler.fit_transform(df[['Age','Annual Income (k$)','Spending Score (1-100)']])
```

3. Apply clustering (KMeans, Hierarchical, DBSCAN) and visualize using `seaborn` or `matplotlib`.

---

This project helps **marketers** target specific customer groups and **mall management** optimize their services for different customer segments.

---