import sklearn
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
 
 
df =  sns.load_dataset("titanic")
 
# drop Cabin column
df.drop(columns=['deck', 'class', 'who', 'adult_male', 'embarked', 'alive'], inplace=True)
 
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['embark_town'], drop_first=False)
 
 
 
 
# Fill NaN values in 'Age' column with mean age of each group, based on 'Sex' and 'Pclass'
def fill_group_age(series: pd.Series) -> pd.Series: # refers to columns
    return series.fillna(series.mean()).round().astype(int)
# df['age'] = df.groupby(['sex', 'pclass'])['age'].transform(fill_group_age)
# OR
# df['Age'] = df.groupby(['Sex', 'Pclass'])['Age'].transform(lambda x: x.fillna(x.mean()).round().astype(int))
 
# Remove statistical outliers(extreme values, aka, ±4 standard deviations) from DataFrame
def remove_outliers_4std(df: pd.DataFrame, cols_to_filter):
    for col in cols_to_filter:
        mean = df[col].mean()
        std = df[col].std()
        df = df[(df[col] >= mean - 4 * std) & (df[col] <= mean + 4 * std)]
    return df
 
# df = remove_outliers_4std(df, ['fare', 'sibsp', 'parch'])
 
def modifications(data_frame : pd.DataFrame):
    data_frame['age'] = data_frame.groupby(['sex', 'pclass'])['age'].transform(fill_group_age)
    data_frame = remove_outliers_4std(data_frame, ['fare', 'sibsp', 'parch'])
    return data_frame
 
# Train/test split with stratification
X_train, X_test, y_train, y_test = train_test_split(df.drop('survived', axis=1), df['survived'], test_size=0.2, random_state=42) # stratify=y
 
# Apply modifications to both training and testing sets
X_train = modifications(X_train)
X_test = modifications(X_test)
y_train = y_train.loc[X_train.index]
y_test  = y_test.loc[X_test.index]
# TODO: Still need standartization or normalization
 
model = LogisticRegression()
model.fit(X_train, y_train)
 
y_pred = model.predict(X_test)
 
from sklearn.metrics import accuracy_score, confusion_matrix
 
 
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)
 
# OR Dovydas example, remove outliers from Series(one column from DataFrame):
# def remove_outliers_4std(series: pd.Series) -> pd.Series:
#     """
#     Removes outliers from a Series that lie beyond 4 standard deviations from the mean.
#     Parameters:
#         series (pd.Series): The input numeric Series.
#     Returns:
#         pd.Series: A filtered Series without outliers.
#     """
#     mean = series.mean()
#     std = series.std()
#     lower_bound = mean - 4 * std
#     upper_bound = mean + 4 * std
#     return series[(series >= lower_bound) & (series <= upper_bound)]
 
 
# print(df.head(20))
# print(df.describe())
# print(df.info())
 
 
# num_unique = df.nunique()
# print(num_unique)
 
 
# sns.histplot(df['deck'])
# plt.show()
 
 
# def drop_objects ( df ):
#     for column in df.columns:
#         if df[column].dtype == "object":
#             df = df.drop (column, axis=1)
#     return df
 
# def fill_average (df, column_name):
#     if column_name in df.columns:
#         average = df[column_name].mean()
#         df[column_name] = df[column_name].fillna(average)
#     return df