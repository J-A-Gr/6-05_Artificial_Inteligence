from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier


# print(df.head(5))
# print(df.describe())
# print(df.info())

# Load your dataset
df = pd.read_csv("data.csv")  # Ensure the file is in the same directory
df.columns = df.columns.str.strip()  # Remove extra spaces

# Select features
features = [
    'ROA(C) before interest and depreciation before interest',
    'Net Income to Total Assets',
    'Debt ratio %',
    'Current Ratio',
    'Quick Ratio',
    'Cash Flow to Total Assets',
    'Liability to Equity',
    'Equity to Liability',
    'Interest Coverage Ratio (Interest expense to EBIT)',
    'Total Asset Turnover',
    'Operating Profit Rate',
    'Bankrupt?'
]

df_selected = df[features]


# Remove statistical outliers(extreme values, aka, ±4 standard deviations) from DataFrame
def remove_outliers_4std(df: pd.DataFrame, cols_to_filter):
    for col in cols_to_filter:
        mean = df[col].mean()
        std = df[col].std()
        df = df[(df[col] >= mean - 4 * std) & (df[col] <= mean + 4 * std)]
    return df

df_selected = remove_outliers_4std(df_selected, df_selected.columns[:-1])  # all but 'Bankrupt?'


# Separate features and target
X = df_selected.drop("Bankrupt?", axis=1)
y = df_selected["Bankrupt?"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.23, random_state=42)

# Scale the features
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)


# Train logistic regression
# model = LogisticRegression(class_weight="balanced", max_iter=1000)
model = KNeighborsClassifier(n_neighbors=20)

model.fit(X_train, y_train)


####################################################################################
"""Class work 06 18"""
####################################################################################
# linear_model = LinearRegression()
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

log_score = cross_val_score(model, X_train, y_train, cv=kfold, scoring="accuracy")
"""accuracy, f1 and roc_auc"""

print(log_score)
print(np.average(log_score))

####################################################################################

"""# Predict on test data"""
y_pred = model.predict(X_test)

# Evaluate model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


##########################################################

sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
# plt.show()