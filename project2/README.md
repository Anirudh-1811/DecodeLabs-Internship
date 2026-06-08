# Multi-Model Machine Learning Benchmark & Production Pipeline
## Project 2 Documentation | DecodeLabs AI Engineering Track

Welcome to the advanced validation and benchmarking repository for the DecodeLabs AI Engineering track. This project demonstrates an automated engineering pipeline designed to handle input sanitization, dynamic hyperparameter tuning, model performance showdown operations, matrix diagnostics, and active production emulation layer deployment.

The architecture evaluates non-linear multi-class boundaries against a scaled representation of classic morphological properties.

---

##  Project Framework Architecture

### Phase 1: Input & Data Handling Layer
Loads the structural matrix properties cleanly from foundational datasets, establishing feature definitions, dynamic dimensional labels, and objective baseline target targets.

### Phase 2: Process Layer (Scaling & Data Splits)
Enforces a structural standard scaler transformation array over the raw features. The dataset is subjected to a randomized 80/20 train/test structural validation split with active data shuffling protocols enabled to eliminate sampling alignment anomalies.

### Phase 3: Multi-Model Benchmark Showdown Suite
Evaluates different algorithmic variants alongside one another. The engine automatically trains an optimized instance of a **K-Nearest Neighbors (KNN)** Classifier alongside a baseline **Linear Logistic Regression** model to contrast parametric and non-parametric boundaries.

### Phase 4: Interactive Production Emulation Testbench
Exposes a continuous input loop interface directly inside the terminal window to serve instant low-latency inference verdicts based on manual structural field data entries.

---

##  Engineering Highlights & Added Features

###  Feature 1: Automated Engine Tuning ("The Elbow Method")
Instead of utilizing fixed assumptions, the engine initiates a dynamic optimization loop spanning $K=1$ to $K=15$. It computes validation testing error configurations dynamically to isolate the lowest validation error signature, configuring the system topology for optimal runtime accuracy.

###  Feature 2 & 4: Multi-Model Showdown Matrix & Advanced Diagnostics
Exhibits system operational tracking results (Accuracy, Macro F1-Coefficient) inside a clean terminal tabular dashboard. It exposes an advanced confusion matrix layer, displaying row-and-column true condition distributions to detect structural bias patterns.

###  Feature 3 & Persistent Storage: Live Deployment Serving Prompt & Logging Engine
Accepts variable data configurations dynamically with internal error protection against bad string typing. Handled metrics are automatically normalized and passed into the fitted pipeline transformation layer. Valid predictions are sequentially saved to a persistent `inference_history.txt` disk file for operational verification logging.

---

##  Dependencies & Installation
Running the benchmark suite requires a standardized Python environment populated with core mathematical processing modules:

```bash
pip install numpy scikit-learn
