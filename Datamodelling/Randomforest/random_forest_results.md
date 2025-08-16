# Random Forest Model for Flood Impact Prediction

## Project Overview
This project uses a **Random Forest Classifier** to predict whether warehouses are impacted by floods based on warehouse-related features.

## Dataset
- Contains information about warehouse characteristics and flood impact.
- Dataset is split into **80% training** and **20% testing**.

## Model Training
- Used `RandomForestClassifier` with:
  - `n_estimators=100`
  - `max_depth=5`
  - `random_state=42`
- Trained on the training dataset.

## Evaluation Results
- **Accuracy:** 0.91  
  Correctly predicts flood impact for ~91% of the test cases.

- **Classification Report:**
  - **Class 0 (Non-Flooded Warehouses):**  
    - Precision: 0.91  
    - Recall: 1.00  
    - F1-Score: 0.95
  - **Class 1 (Flooded Warehouses):**  
    - Precision: 0.50  
    - Recall: 0.05  
    - F1-Score: 0.09
  - **Macro Average:** Precision 0.70 | Recall 0.52 | F1-Score 0.52  
  - **Weighted Average:** Precision 0.87 | Recall 0.91 | F1-Score 0.88  

- The model performs very well for **non-flooded warehouses**, but struggles with correctly detecting **flooded warehouses** due to class imbalance.

<img width="306" height="137" alt="{77A115DC-28FA-4F3E-A87F-D882A50DC374}" src="https://github.com/user-attachments/assets/49646c01-717a-4cf2-8588-2e404d2bb15d" />
