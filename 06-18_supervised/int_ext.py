from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.calibration import LabelEncoder
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline


df = pd.read_csv("personality_dataset (2).csv")


# df.dropna(how='any', inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)
# print(df.head(5))
# print(df.describe())
# print(df.info())

# 2. Encode all object columns (including Yes/No and Personality)
label_encoders = {}
for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = df[col].astype(str)  # Just in case there's a mix of strings/nan
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

# 3. Split into X and y
X = df.drop(columns=["Personality"])
y = df["Personality"]


# ----- MODELING -----

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=95)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Predict and evaluate
y_pred = knn.predict(X_test_scaled)

# Inverse transform y for readable class names
target_le = label_encoders["Personality"]
y_test_labels = target_le.inverse_transform(y_test)
y_pred_labels = target_le.inverse_transform(y_pred)

print("Classification Report:\n")
print(classification_report(y_test_labels, y_pred_labels))

# Confusion Matrix
cm = confusion_matrix(y_test_labels, y_pred_labels)
sns.heatmap(cm, annot=True, fmt="d",
            xticklabels=target_le.classes_,
            yticklabels=target_le.classes_,
            cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("KNN Confusion Matrix")
plt.show()

# Cross-validation
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=7))
])
cv_scores = cross_val_score(pipeline, X, y, cv=7)
print("Cross-validation scores:", cv_scores)
print("Mean CV accuracy:", cv_scores.mean())