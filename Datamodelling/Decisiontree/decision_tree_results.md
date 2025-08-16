# Decision Tree Results

## Data Preprocessing
- Converted categorical variables (`WH_capacity_size`, `Location_type`, `zone`, `WH_regional_zone`, `wh_owner_type`, `approved_wh_govt_certificate`) into numeric codes.
- Split dataset into **80% training** and **20% testing**.

## Model Training
- Used `DecisionTreeClassifier` with `max_depth=5` to prevent overfitting.
- Trained the model on the training dataset.

## Evaluation

### Accuracy Score
- **Accuracy:** 0.9  
  The model correctly predicts flood impact for **90%** of the test cases.

### Classification Report
- **Class 0 (Non-Flooded Warehouses):**
  - Precision: 0.90 → When the model predicts a warehouse is not impacted by floods, it is correct 90% of the time.
  - Recall: 1.00 → The model correctly identifies all actual non-flooded warehouses.
  - F1-Score: 0.95 → Strong balance of precision and recall for this class.

- **Class 1 (Flooded Warehouses):**
  - Precision: 0.33 → When the model predicts a warehouse is impacted by floods, it is correct only 33% of the time.
  - Recall: 0.01 → Out of all actual flooded warehouses, the model identifies only 1%.
  - F1-Score: 0.02 → Very low, highlighting poor performance in identifying flood-impacted warehouses.

- **Macro Average:**
  - Precision: 0.62, Recall: 0.50, F1-Score: 0.48 → Shows overall performance is affected by difficulty in predicting the minority class (flooded warehouses).

- **Weighted Average:**
  - Precision: 0.85, Recall: 0.90, F1-Score: 0.86 → High overall performance, influenced mainly by the dominant class (non-flooded warehouses).

### Confusion Matrix
![Confusion Matrix](https://github.com/user-attachments/assets/2aca98e9-8c9d-4087-a4a3-4fccb3adf9b6)
