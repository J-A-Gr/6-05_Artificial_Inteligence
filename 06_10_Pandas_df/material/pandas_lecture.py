import numpy as np
import pandas as pd


df = pd.read_csv("personality_dataset.csv")


print(df.head())


numerical_df = df.select_dtypes(include=[np.number])

print(numerical_df.head())

correlation_matrix = numerical_df.corr()
print(correlation_matrix)




# df_new = df[df["Stage_fear"] == "No"]

# df_new = df[["Personality", "Going_outside"]] # paiimti stulpelius

# df_new = df_new[df_new["Going_outside"].notnull()] # išimam nulines reikšmes

# print(df_new.iloc[2]) # paiiimti eilute
# # print(df_new.iloc[0:10:2]) # paiiimti eilute
# print(df_new.iloc[-10:]) # paiiimti eilute
# # print(df_new.describe())
# print(df_new.info())

# df_new = df_new[df_new["Going_outside"] < 3]

# df_new_introvert = df_new[df_new["Personality"] == "Introvert"]

# df_new_extrovert = df_new[df_new["Personality"] == "Extrovert"]

# df_new_introvert = df_new_introvert.sort_values("Going_outside") # rušiuoti
# df_new_extrovert = df_new_extrovert.sort_values("Going_outside") # rušiuoti


# null_df = df["Going_outside"].isnull()

# print(null_df)
# print(null_df.value_counts())


# null_all_df = df[df["Going_outside"].isnull()]


# null_all_df.to_csv("data/export_null_all_df.csv",index=False)



# print(df_new_introvert.value_counts())
# print(df_new_extrovert.value_counts())

# df_new_introvert = df_new_introvert.rename(
#     columns={
#         "Personality": "Asmenybė", 
#         "Going_outside": "Eina_i_lauka"
#         }
#     )

# df_new_introvert.replace("Introvert", "Intravertas", inplace=True)

# df_new_extrovert = df_new_extrovert.rename(
#     columns={
#         "Personality": "Asmenybė", 
#         "Going_outside": "Eina_i_lauka"
#         }
#     )

# df_new_extrovert.replace("Extrovert", "Extravertas", inplace=True)

# df_new_introvert["Mūsų išvada"] = [None for x in range(len(df_new_introvert))]

# df_new_introvert["Mūsų išvada"] = df_new_introvert["Eina_i_lauka"].apply(lambda x: "Extravertas" if x > 2 else "Intravertas")

# df_new_introvert["Mūsų išvada"] = ["Extravertas" if x > 2 else "Intravertas" for x in df_new_introvert["Eina_i_lauka"]]

# def categorize_personalities(going_outside_score):

#     if going_outside_score < 1:
#         return "Stiptus introvertas"
#     elif going_outside_score < 3:
#         return "Truputi introvertas"
#     elif going_outside_score == 3:
#         return "Ambivertas"
#     elif going_outside_score <=5:
#         return "Truputi extrovertas"
#     else:
#         return "Stiptus extrovertas"




# df_new_introvert["Mūsų išvada"] = df_new_introvert["Eina_i_lauka"].apply(categorize_personalities)


# df_new_introvert.to_csv("data/export_introvert.csv",index=False)
# df_new_extrovert.to_csv("data/export_extrovert.csv",index=False)






# print(df_new_introvert.transpose())
