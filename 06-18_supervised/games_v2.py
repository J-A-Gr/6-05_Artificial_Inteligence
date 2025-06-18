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

# 3. Remove outliers (±4 std from mean on all numeric columns except target)
def remove_outliers_4std(df, cols_to_filter):
    for col in cols_to_filter:
        mean = df[col].mean()
        std = df[col].std()
        df = df[(df[col] >= mean - 4 * std) & (df[col] <= mean + 4 * std)]
    return df

df = remove_outliers_4std(df, ["Year"])
df = remove_outliers_4std(df, ["Global_Sales"])

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
print(" MSE :", mean_squared_error(y_test_orig, y_pred_orig))
print(" MAE :", mean_absolute_error(y_test_orig, y_pred_orig))
print(" R²  :", r2_score(y_test_orig, y_pred_orig))

cv_r2 = cross_val_score(model, X, np.log1p(y), cv=5, scoring="r2")
print("\n5-Fold CV R² on log1p(y):", cv_r2)
print("Mean CV R²:", cv_r2.mean())

# print(df.head())
# print(df.describe())