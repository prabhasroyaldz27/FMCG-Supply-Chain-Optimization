# random_forest_model.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -------------------------------
# Load the dataset
# -------------------------------
# Replace with your actual dataset path
data = pd.read_csv("FMCG_data.csv")

# -------------------------------
# Define features and target variable
# -------------------------------
X = data[['WH_capacity_size', 'workers_num', 'distributor_num', 'dist_from_hub', 'retail_shop_num']]
y = data['flood_impacted']

# -------------------------------
# Split into train/test
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Train Random Forest Classifier
# -------------------------------
rf_clf = RandomForestClassifier(
    n_estimators=100, 
    max_depth=5, 
    random_state=42
)
rf_clf.fit(X_train, y_train)

# -------------------------------
# Predictions
# -------------------------------
y_pred_rf = rf_clf.predict(X_test)

# -------------------------------
# Evaluation
# -------------------------------
print("Random Forest Accuracy Score:", accuracy_score(y_test, y_pred_rf))
print("Random Forest Classification Report:\n", classification_report(y_test, y_pred_rf))

# -------------------------------
# Confusion Matrix
# -------------------------------
cm = confusion_matrix(y_test, y_pred_rf)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues",
            xticklabels=['Non-Flooded', 'Flooded'],
            yticklabels=['Non-Flooded', 'Flooded'])
plt.title("Confusion Matrix - Random Forest")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.show()
