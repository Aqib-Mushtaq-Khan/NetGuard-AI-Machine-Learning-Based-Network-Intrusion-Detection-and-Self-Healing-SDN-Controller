import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    ConfusionMatrixDisplay
)
from sklearn.preprocessing import LabelEncoder


# Step 1: Load dataset
df = pd.read_csv("data/raw/network_traffic.csv")

print("Dataset loaded successfully.")
print("Dataset shape:", df.shape)
print(df.head())

# Step 2: Separate input features and output label
X = df.drop(columns=["label"])
y_text = df["label"]

# Step 3: Convert labels from text to numbers
encoder = LabelEncoder()
y = encoder.fit_transform(y_text)

print("\nClasses found:")
print(list(encoder.classes_))

# Step 4: Split data into training and testing parts
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# Step 5: Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)

# Step 6: Train the model
model.fit(X_train, y_train)

# Step 7: Test the model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel trained successfully.")
print("Accuracy:", accuracy)

report = classification_report(
    y_test,
    predictions,
    target_names=encoder.classes_
)

print("\nClassification Report:")
print(report)

# Step 8: Create folders for saved results
os.makedirs("models", exist_ok=True)
os.makedirs("results", exist_ok=True)

# Step 9: Save model and label encoder
joblib.dump(model, "models/netguard_model.pkl")
joblib.dump(encoder, "models/label_encoder.pkl")

print("\nModel saved in models/netguard_model.pkl")
print("Label encoder saved in models/label_encoder.pkl")

# Step 10: Save classification report
with open("results/classification_report.txt", "w") as f:
    f.write(f"Accuracy: {accuracy}\n\n")
    f.write(report)

print("Classification report saved in results/classification_report.txt")

# Step 11: Save confusion matrix
ConfusionMatrixDisplay.from_estimator(
    model,
    X_test,
    y_test,
    display_labels=encoder.classes_
)

plt.title("NetGuard-AI Confusion Matrix")
plt.savefig("results/confusion_matrix.png", dpi=300, bbox_inches="tight")
plt.close()

print("Confusion matrix saved in results/confusion_matrix.png")

# Step 12: Save feature importance
feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
}).sort_values(by="importance", ascending=False)

feature_importance.to_csv("results/feature_importance.csv", index=False)

plt.figure(figsize=(8, 5))
plt.bar(feature_importance["feature"], feature_importance["importance"])
plt.xticks(rotation=45, ha="right")
plt.title("NetGuard-AI Feature Importance")
plt.xlabel("Network Feature")
plt.ylabel("Importance")
plt.tight_layout()
plt.savefig("results/feature_importance.png", dpi=300)
plt.close()

print("Feature importance saved in results/feature_importance.png")
print("\nTraining pipeline completed successfully.")