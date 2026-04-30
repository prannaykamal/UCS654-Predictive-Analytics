# Clustering Assignment

## 📌 Objective
To perform a comparative performance study of different clustering algorithms using different preprocessing techniques and varying number of clusters.

---

## 📊 Dataset
- Iris Dataset (from sklearn / UCI Repository)
- Total Samples: 150
- Features: 4

---

## ⚙️ Algorithms Used
1. K-Means Clustering
2. Hierarchical Clustering (Agglomerative)
3. Mean Shift Clustering

---

## 🔄 Preprocessing Techniques
- No Data Processing
- Normalization (StandardScaler)
- PCA (Principal Component Analysis)
- Normalization + PCA

---

## 📏 Evaluation Metrics
- Silhouette Score (Higher is better)
- Calinski-Harabasz Score (Higher is better)
- Davies-Bouldin Score (Lower is better)

---

## 📊 Results

### 🔹 K-Means Clustering

| Clusters | Preprocessing | Silhouette | Calinski-Harabasz | Davies-Bouldin |
|---------|--------------|------------|-------------------|----------------|
| 3 | No Processing | 0.551 | 561.59 | 0.666 |
| 3 | Normalization | 0.459 | 241.90 | 0.833 |
| 3 | PCA | 0.597 | 693.70 | 0.564 |
| 3 | Norm + PCA | 0.509 | 293.85 | 0.709 |

| 4 | No Processing | 0.498 | 530.76 | 0.780 |
| 4 | Normalization | 0.386 | 207.26 | 0.869 |
| 4 | PCA | 0.560 | 715.90 | 0.619 |
| 4 | Norm + PCA | 0.457 | 261.70 | 0.723 |

| 5 | No Processing | 0.460 | 459.45 | 0.915 |
| 5 | Normalization | 0.345 | 203.26 | 0.945 |
| 5 | PCA | 0.545 | 683.67 | 0.648 |
| 5 | Norm + PCA | 0.425 | 274.81 | 0.753 |

---

### 🔹 Hierarchical Clustering

| Clusters | Preprocessing | Silhouette | Calinski-Harabasz | Davies-Bouldin |
|---------|--------------|------------|-------------------|----------------|
| 3 | No Processing | 0.554 | 558.05 | 0.656 |
| 3 | Normalization | 0.446 | 222.71 | 0.803 |
| 3 | PCA | 0.598 | 688.61 | 0.560 |
| 3 | Norm + PCA | 0.511 | 286.32 | 0.705 |

| 4 | No Processing | 0.488 | 515.07 | 0.795 |
| 4 | Normalization | 0.400 | 201.25 | 0.978 |
| 4 | PCA | 0.540 | 673.94 | 0.654 |
| 4 | Norm + PCA | 0.448 | 254.09 | 0.722 |

| 5 | No Processing | 0.484 | 488.48 | 0.820 |
| 5 | Normalization | 0.330 | 192.68 | 0.974 |
| 5 | PCA | 0.548 | 665.88 | 0.652 |
| 5 | Norm + PCA | 0.404 | 254.99 | 0.791 |

---

### 🔹 Mean Shift Clustering

| Preprocessing | Silhouette | Calinski-Harabasz | Davies-Bouldin |
|--------------|------------|-------------------|----------------|
| No Processing | 0.685 | 509.70 | 0.388 |
| Normalization | 0.581 | 251.34 | 0.593 |
| PCA | 0.710 | 565.73 | 0.355 |
| Norm + PCA | 0.614 | 283.00 | 0.543 |

---

## 📈 Visualization

Example of K-Means clustering using PCA:

![KMeans Graph](kmeans_pca.png)

---

## 📌 Observations
- PCA significantly improves clustering performance
- Mean Shift gives highest silhouette score in many cases
- Normalization alone sometimes reduces performance
- Best results are generally obtained using PCA

---

## 📊 Conclusion
- PCA is the most effective preprocessing technique
- Mean Shift performs best overall without specifying clusters
- K-Means and Hierarchical give similar results
- Number of clusters affects performance significantly

---

## 🚀 How to Run
1. Open the notebook in Google Colab
2. Run all cells
3. View output and graphs

---

## 👨‍💻 Author
* Name - Manmeet Singh 
* Roll no - 102317039
