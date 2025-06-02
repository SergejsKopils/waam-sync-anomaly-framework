import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, jaccard_score

# === 1. Load CSV files ===
df_gt = pd.read_csv("src/1MethodGroundTruth/output/1MethodGroundTruth.csv")
df_kmeans_known = pd.read_csv("src/2MethodClusterKMeansKnown/output/2MethodClusterKMeansKnown.csv")
df_kmeans_auto = pd.read_csv("src/3MethodClusterKMeansAuto/output/3MethodClusterKMeansAuto.csv")
df_dbscan = pd.read_csv("src/4MethodClusterDBSCANAuto/output/4MethodClusterDBSCAN_result.csv")
df_geometry = pd.read_csv("src/5MethodGeometryBased/output/5MethodGeometryBased.csv")
df_hierarchical = pd.read_csv("src/6MethodHierarchicalAuto/output/6MethodHierarchicalAuto.csv")

# === 2. Function to compare predictions by coordinates ===
def compare_by_coordinates(df_pred, df_gt, col_pred, col_gt="layer_id_1MethodGroundTruth"):
    merged = pd.merge(
        df_gt[['X', 'Y', 'Z', col_gt]],
        df_pred[['X', 'Y', 'Z', col_pred]],
        on=['X', 'Y', 'Z'], how='inner'
    )
    
    y_true = merged[col_gt]
    y_pred = merged[col_pred]
    
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision (macro)": precision_score(y_true, y_pred, average='macro', zero_division=0),
        "Recall (macro)": recall_score(y_true, y_pred, average='macro', zero_division=0),
        "F1-score (macro)": f1_score(y_true, y_pred, average='macro', zero_division=0),
        "IoU (macro)": jaccard_score(y_true, y_pred, average='macro', zero_division=0)
    }

# === 3. Compare all methods ===
results = []
methods = [
    ("2Method_KMeansKnown", df_kmeans_known, df_kmeans_known.filter(like="layer_id").columns[0]),
    ("3Method_KMeansAuto", df_kmeans_auto, df_kmeans_auto.filter(like="layer_id").columns[0]),
    ("4Method_DBSCAN", df_dbscan, df_dbscan.filter(like="layer_id").columns[0]),
    ("5Method_Geometry", df_geometry, df_geometry.filter(like="layer_id").columns[0]),
    ("6Method_HierarchicalAuto", df_hierarchical, df_hierarchical.filter(like="layer_id").columns[0]),
]

for method_name, df_method, col_name in methods:
    scores = compare_by_coordinates(df_method, df_gt, col_name)
    scores["Method"] = method_name
    results.append(scores)

# === 4. Display results ===
df_results = pd.DataFrame(results).set_index("Method")
df_results = df_results.round(3) * 100

print("\n=== Comparison of clustering methods against ground truth ===\n")
print(df_results.to_markdown())

# Save to CSV
df_results.to_csv("src/compare_metrics_results.csv")
