# WAAM Sync + Anomaly Framework

This repository contains a modular Python-based framework for synchronization, segmentation, and anomaly detection in Wire Arc Additive Manufacturing (WAAM) using multi-stream data (scanner, process logs, control commands).

## 📁 Submodules Overview

### `1MethodGroundTruth`
This module contains the reference segmentation based on scan-derived layer structure. It serves as ground truth for evaluating other methods.

### `2MethodClusterKMeansKnown`
KMeans clustering by Z coordinate with a predefined number of layers (n_clusters=7). Used to segment layers from 3D scan data.

### `3MethodClusterKMeansAuto`
KMeans clustering with automatic layer count estimation. Identifies layers based on statistical Z-distribution.

### `4MethodClusterDBSCANAuto`
DBSCAN clustering based on Z-values. Automatically finds dense layer-like regions without needing the number of clusters.

### `5MethodGeometryBased`
Geometry-based segmentation by detecting distance jumps. Aligns scan structure with process log and control commands.

### `6MethodHierarchicalAuto`
Hierarchical clustering applied to Z-values for automatic layer segmentation. Useful when clusters are nested or uneven.

### `AnomalyDetection`
Rule-based anomaly detection module. Flags irregular regions based on layer geometry and process parameters.

### `ProcessData_ClusterByZ_DBSCAN`
Clustering of WAAM process data (e.g. robot logs) by height. Separates deposition segments using DBSCAN.

### `ProcessDataIntegration`
Integrates process logs, scan points, and G-code. Prepares the full synchronized dataset for visualization and anomaly analysis.
