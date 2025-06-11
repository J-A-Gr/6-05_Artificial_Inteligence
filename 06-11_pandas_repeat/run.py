import pandas as pd
import numpy as np

df = pd.read_csv("personality_dataset.csv")
print(df)

df_new = df[['Personality', 'Time_spent_Alone']]
df_new = df_new.sort_values(by='Time_spent_Alone', ascending=True)
# print(df_new)


null_df = df_new['Time_spent_Alone'].isnull()
print(null_df.value_counts())

print(df_new)


df_new.to_csv('hidden_gem.csv', index=False)

ok = np.zeros(1378)
print(ok)