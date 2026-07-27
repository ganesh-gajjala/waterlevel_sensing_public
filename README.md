# Geothermal Well Fluid Level Detector
### 📈 Executive Summary

* **The Problem:** Deep geothermal well monitoring generates vast, noisy streams of continuous time-series temperature data via fiber-optic distributed temperature sensing (DTS) cables, making manual identification of dynamic water levels labor-intensive and prone to error.
* **The Computational Solution:** Developed a robust Python pipeline that applies unsupervised machine learning (clustering algorithms) and statistical pattern recognition to automatically filter signal noise and isolate structural thermal boundaries.
* **The Domain Impact:** Enables automated, real-time tracking of fluid levels in deep geothermal wells, drastically improving early anomaly detection and operational safety frameworks for clean energy infrastructure.

Automated Python workflow designed to process high-frequency distributed temperature sensing (DTS) data collected via optical fibers. The system leverages unsupervised machine learning to detect shifting fluid levels and gas/liquid phase transitions within deep geothermal wells under varying operational loads.

## 📋 Overview & Problem Statement

Fluid levels in deep geothermal wells fluctuate dynamically based on submersible pump operations. This repository isolates the exact depth where the **gas phase transitions into the fluid phase** across three core operational states:
1. **Full Capacity:** Peak draw-down depth.
2. **Reduced Capacity:** Intermediate fluid equilibrium depth.
3. **Static / Not Operating:** Maximum fluid recovery height.

The structural requirement of this codebase is to benchmark and deploy a single, robust machine learning algorithm capable of automatically identifying the fluid-gas boundary layer across all three dynamic pump profiles without requiring manual scenario flagging.

## 🛠️ Core Script Architecture

The repository contains modular exploration scripts tailored to specific algorithmic approaches:

*   `clustering_HDBSCAN.py`: Ingests time-interval temperature matrices and employs Density-Based Spatial Clustering of Applications with Noise (`HDBSCAN`) to isolate thermal gradients, mapping the gas phase, fluid phase, and water level boundary.
*   `clustering_KMeans.py`: Utilizes centroid-based partitioning (`K-Means`) to segment the well's vertical profile into distinct thermal/physical zones to locate the interface layer.

## 📦 Requirements & Installation

1. Clone the repository to your internal environment:
   ```bash
   git clone https://github.com
   cd geothermal-fluid-detector
   ```

2. Install the necessary data science stack and log-parsing dependencies:
   ```bash
   pip install numpy pandas scikit-learn hdbscan dlisio
   ```

## 🚀 How to Use

1. Place your time-series optical fiber temperature logs into the designated project data directory.
2. Execute the evaluation scripts to parse data slices and view phase results:
   ```bash
   python clustering_HDBSCAN.py
   python clustering_KMeans.py
   ```

## 🔮 Prospective Outlook & Roadmap

*   **Option 1 (Hyperparameter Optimization):** Fine-tune the `min_cluster_size` and `min_samples` density constraints within the HDBSCAN algorithm to tighten boundary line detection accuracy where the fluid phase transitions into gas.
*   **Option 2 (Alternative Model Benchmarking):** Expand tests to evaluate alternative clustering architectures suited for spatial gradient boundaries, including:
    *   `Birch` (Balanced Iterative Reducing and Clustering using Hierarchies)
    *   `FeatureAgglomeration` (Hierarchical feature grouping)
    *   `Gaussian Mixture Models (GMM)` (Probabilistic density boundary mapping)

## ⚠️ Internal Notice

🔒 **Confidentiality:** This repository is intended strictly for **internal use only**. Do not distribute, publish, or share data/code blocks externally without explicit organizational clearance.
