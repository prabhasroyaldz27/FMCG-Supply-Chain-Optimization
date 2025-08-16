import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load dataset
data = pd.read_csv("data/FMCG_data.csv")

# Encode categorical variables
data['WH_capacity_size'] = data['WH_capacity_size'].replace({"Small": 1, "Mid": 2, "Large": 3})
data['Location_type'] = data['Location_type'].astype('category').cat.codes
data['zone'] = data['zone'].astype('category').cat.codes
data['WH_regional_zone'] = data['WH_regional_zone'].astype('category').cat.codes
data['wh_owner_type'] = data['wh_owner_type'].astype('category').cat.codes
data['approved_wh_govt_certificate'] = data['approved_wh_govt_certificate'].map({"Yes": 1, "No": 0})

# Features & Target
X = data.drop(columns=['target'])   # replace 'target' with actual target column name
y = data['target']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree Model
clf = DecisionTreeClassifier(random_state=42, max_depth=5)
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Evaluation
acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Decision Tree Accuracy:", acc)
print("\nClassification Report:\n", report)

# Save model
joblib.dump(clf, "decision_tree_model.pkl")

# Confusion matrix visualization
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=set(y), yticklabels=set(y))
plt.title("Decision Tree Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("decision_tree_metrics.png")
plt.close()

# Save feature importance visualization
importances = clf.feature_importances_
feat_names = X.columns
plt.figure(figsize=(8,5))
sns.barplot(x=importances, y=feat_names)
plt.title("Feature Importance - Decision Tree")
plt.savefig("decision_tree_feature_importance.png")
plt.close()

# Save tree rules as text
with open("decision_tree_rules.txt", "w") as f:
    f.write(export_text(clf, feature_names=list(X.columns)))
