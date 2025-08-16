# Gradient Boosting Model for Flood Impact Prediction

## Project Overview
This project uses a **Gradient Boosting Classifier** to predict whether warehouses are impacted by floods based on warehouse-related features.

## Dataset
- Contains information about warehouse characteristics and flood impact.
- Dataset is split into **80% training** and **20% testing**.

## Model Training
- Used `GradientBoostingClassifier` with:
  - `n_estimators=100`
  - `learning_rate=0.1`
  - `max_depth=5`
  - `random_state=42`
- Trained on the training dataset.

## Evaluation Results
- **Accuracy:** 0.8985  
  Correctly predicts flood impact for ~90% of the test cases.

- **Classification Report:**
  - **Class 0 (Non-Flooded Warehouses):**  
    - Precision: 0.90  
    - Recall: 1.00  
    - F1-Score: 0.95
  - **Class 1 (Flooded Warehouses):**  
    - Precision: 0.27  
    - Recall: 0.02  
    - F1-Score: 0.03
  - **Macro Average:** Precision 0.59 | Recall 0.51 | F1-Score 0.49  
  - **Weighted Average:** Precision 0.84 | Recall 0.90 | F1-Score 0.86  

- The model performs very well for **non-flooded warehouses**, but struggles with correctly detecting **flooded warehouses** due to class imbalance.

## Visualization
<img width="478" height="185" alt="Gradient Boosting Results" src="https://github.com/user-attachments/assets/c487028a-178f-4499-8315-b6a4f6fb5b82" />

