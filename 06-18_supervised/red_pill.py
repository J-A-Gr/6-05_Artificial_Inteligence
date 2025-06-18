# # mapinam i yes/no, kad nebutu overkill su labelencoderiu.
# yes_no_columns = ["Stage_fear", "Drained_after_socializing"]
# for col in yes_no_columns:
#     df[col] = df[col].map({"No": 0, "Yes": 1})

# # Encode target
# label_encoder = LabelEncoder()
# y = label_encoder.fit_transform(df["Personality"])  # Encoded labels: Extrovert → 0, Introvert → 1
# X = df.drop(columns=["Personality"])