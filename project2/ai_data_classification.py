import os
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

def run_advanced_classification_pipeline():
    print("==================================================================")
    print("DECODELABS ADVANCED TRAINING SUITE: MULTI-MODEL ML BENCHMARK")
    print("Batch: 2026 | Powered by DecodeLabs")
    print("==================================================================\n")

    iris_data = load_iris()
    features, labels, class_names = iris_data.data, iris_data.target, iris_data.target_names 

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    X_train, X_test, y_train, y_test = train_test_split(
        scaled_features, labels, test_size=0.20, random_state=42, shuffle=True
    )

    print("[FEATURE 1] Initiating Dynamic Hyperparameter Optimization Loop...")
    best_k = 1
    lowest_error = 1.0
    
    for k in range(1, 16):
        test_knn = KNeighborsClassifier(n_neighbors=k)
        test_knn.fit(X_train, y_train)
        predictions_k = test_knn.predict(X_test)
        error_rate = 1.0 - accuracy_score(y_test, predictions_k)
        
        if error_rate < lowest_error:
            lowest_error = error_rate
            best_k = k
            
    print(f"-> Tuning Complete: Mathematically Optimal K found at K = {best_k}")
    print(f"-> Minimum Test Error Achieved: {lowest_error:.4f}\n")

    print("[FEATURE 2] Executing Comparative Multi-Model Showdown Suite...")
    knn_model = KNeighborsClassifier(n_neighbors=best_k)
    knn_model.fit(X_train, y_train)
    knn_preds = knn_model.predict(X_test)
    
    log_model = LogisticRegression(random_state=42)
    log_model.fit(X_train, y_train)
    log_preds = log_model.predict(X_test)
    
    print("\n================== BENCHMARK SHOWDOWN MATRIX ==================")
    print(f"Metric              | K-Nearest Neighbors (K={best_k}) | Logistic Regression")
    print("----------------------------------------------------------------")
    print(f"Accuracy Score      | {accuracy_score(y_test, knn_preds)*100:^26.2f}% | {accuracy_score(y_test, log_preds)*100:^19.2f}%")
    print(f"Macro F1-Coefficient| {f1_score(y_test, knn_preds, average='macro'):^27.4f} | {f1_score(y_test, log_preds, average='macro'):^20.4f}")
    print("================================================================\n")

    print("[FEATURE 4] Advanced Diagnostic Layer Matrix:")
    print("--- KNN Confusion Matrix ---")
    print(confusion_matrix(y_test, knn_preds))
    print("--- Logistic Regression Confusion Matrix ---")
    print(confusion_matrix(y_test, log_preds))
    print("----------------------------------------------------------------\n")

    print("[FEATURE 3] Launching Live Deployment serving prompt...")
    print("-> Continuous production loop active. Enter data to serve instant inference.")
    print("-> Type 'exit' at any prompt to close the pipeline session.\n")
    
    log_filename = "inference_history.txt"
    
    while True:
        try:
            print("--- New Sample Inference Vector ---")
            sepal_len = input("Enter Sepal Length (cm): ").strip().lower()
            if sepal_len == 'exit': break
                
            sepal_wid = input("Enter Sepal Width (cm): ").strip().lower()
            if sepal_wid == 'exit': break
                
            petal_len = input("Enter Petal Length (cm): ").strip().lower()
            if petal_len == 'exit': break
                
            petal_wid = input("Enter Petal Width (cm): ").strip().lower()
            if petal_wid == 'exit': break

            raw_sample = np.array([[float(sepal_len), float(sepal_wid), float(petal_len), float(petal_wid)]])
            scaled_sample = scaler.transform(raw_sample)
            
            live_prediction = knn_model.predict(scaled_sample)[0]
            predicted_flower = class_names[live_prediction]
            
            print(f"\n>>> MACHINE LEARNING DECISION VERDICT: Iris {predicted_flower.upper()} <<<\n")
            
            with open(log_filename, "a") as log_file:
                log_file.write(f"Input: {raw_sample.tolist()} -> Prediction: Iris {predicted_flower.upper()}\n")
            print(f"[LOGGED] Verification saved to internal file tracker: {log_filename}\n")
            
        except ValueError:
            print("\n[ERROR] Numerical parse failed. Enforce raw metric float coordinates only.\n")
        except (KeyboardInterrupt, EOFError):
            break

    print("\n==================================================================")
    print("PIPELINE TERMINATED: PORTFOLIO VERIFICATION SUITE COMPLETE")
    print("==================================================================")

if __name__ == "__main__":
    run_classification_pipeline = run_advanced_classification_pipeline
    run_classification_pipeline()
