import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load & drop
df = pd.read_csv("vgsales.csv").drop(
    columns=["Rank","Name","NA_Sales","EU_Sales","JP_Sales","Other_Sales"])


# print(df.info())
df["Year"] = df["Year"].fillna(df["Year"].median())
df["Publisher"] = df["Publisher"].fillna("Unknown")

print(df.describe())

# print(df.info())

# Remove statistical outliers(extreme values, aka, ±4 standard deviations) from DataFrame
def remove_outliers_4std(df: pd.DataFrame, cols_to_filter):
    for col in cols_to_filter:
        mean = df[col].mean()
        std = df[col].std()
        df = df[(df[col] >= mean - 4 * std) & (df[col] <= mean + 4 * std)]
    return df

df_selected = remove_outliers_4std(df, df.columns[:-1]) # all but global sales


######
top_publishers = df_selected["Publisher"].value_counts().nlargest(20).index
df_selected["Publisher"] = df_selected["Publisher"].where(
    df_selected["Publisher"].isin(top_publishers), "Other"
)

df_selected["Year"] = df_selected["Year"].fillna(df_selected["Year"].median())
y = df_selected["Global_Sales"]
X = df_selected.drop(columns="Global_Sales")


# 3. Pipeline:  
#   - numeric: nothing but scale  
#   - categorical: impute + one-hot  
#   - log1p on target via FunctionTransformer
pipeline = Pipeline([
    ("preprocess", 
        # ColumnTransformer isn’t strictly necessary for just 1 numeric + 3 cats, 
        # but still useful to see intent
        ColumnTransformer([
            ("num", StandardScaler(), ["Year"]),
            ("cat", OneHotEncoder(handle_unknown="ignore"), ["Platform","Genre","Publisher"])
        ])
    ),
    ("model", LinearRegression()),
])




# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, np.log1p(y),  # log1p here to tame skew
    test_size=0.25,random_state=42)

# 5. Fit & evaluate on hold-out
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
y_pred_orig = np.expm1(y_pred)
y_test_orig = np.expm1(y_test)

# print("Hold-out Results (back on original scale):")
# print(" MSE :", mean_squared_error(y_test_orig, y_pred_orig))
# print(" MAE :", mean_absolute_error(y_test_orig, y_pred_orig))
# print(" R²  :", r2_score(y_test_orig, y_pred_orig))

# 6. 5-fold CV on log-target (R² is invariant to monotonic transforms)
cv_r2 = cross_val_score(
    pipeline, X, np.log1p(y), cv=5, scoring="r2"
)
print("\n5-Fold CV R² on log1p(y):", cv_r2)
print("Mean CV R²:", cv_r2.mean())
