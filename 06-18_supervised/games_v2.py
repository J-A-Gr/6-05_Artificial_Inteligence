import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load & drop
df = pd.read_csv("vgsales.csv").drop(
    columns=["Rank", "Name"] # , "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"
)

# 2. Handle missing values
df["Year"] = df["Year"].fillna(df["Year"].median())
df["Publisher"] = df["Publisher"].fillna("Unknown")

# 4. Reduce Publisher cardinality
top_publishers = df["Publisher"].value_counts().nlargest(20).index
df["Publisher"] = df["Publisher"].where(df["Publisher"].isin(top_publishers), "Other")

# 5. One-hot encode categorical columns
df = pd.get_dummies(df, columns=["Platform", "Genre", "Publisher"], drop_first=True)

# 6. Prepare features and target
y = df["Global_Sales"]
X = df.drop(columns="Global_Sales")

# 7. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, np.log1p(y), test_size=0.25, random_state=42
)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred_orig = np.expm1(y_pred)
y_test_orig = np.expm1(y_test)

print("Hold-out Results (RandomForest):")
print(" MSE :", mean_squared_error(y_test_orig, y_pred_orig)) # (Mean Squared Error) | Lower is better. Squaring penalizes larger errors more strongly. 
print(" MAE :", mean_absolute_error(y_test_orig, y_pred_orig)) # (Mean Absolute Error) | A value of 'result' means the model’s predictions are off by ~0.0212 units on average.
print(" R²  :", r2_score(y_test_orig, y_pred_orig))  # Ranges from 0 (model explains nothing) to 1 (perfect explanation).

# Perform 5-fold cross-validation
cv_scores = cross_val_score(model, X, np.log1p(y), cv=5, scoring="r2")

print(f"5-Fold CV R² scores: {cv_scores}")
print(f"Mean CV R²: {cv_scores.mean():.4f}")
# print(df.head())
# print(df.describe())