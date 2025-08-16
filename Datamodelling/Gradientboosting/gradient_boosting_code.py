import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset (make sure FMCG_data.csv is in the same folder as this script)
data = pd.read_csv('FMCG_data.csv')

# Define features and target variable
X = data[['WH_capacity_size', 'workers_num', 'distributor_num', 'dist_from_hub', 'retail_shop_num']]
y = data['flood_impacted']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Gradient Boosting Classifier
gb_clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
gb_clf.fit(X_train, y_train)

# Make predictions and evaluate
y_pred_gb = gb_clf.predict(X_test)

print("Gradient Boosting Accuracy Score:", accuracy_score(y_test, y_pred_gb))
print("Gradient Boosting Classification Report:\n", classification_report(y_test, y_pred_gb))
