import pandas as pd
import numpy as np

"""1"""
df = pd.read_csv('train.csv')
# print(df)

"""2"""

missing_values = df.isnull().sum()
print(missing_values)