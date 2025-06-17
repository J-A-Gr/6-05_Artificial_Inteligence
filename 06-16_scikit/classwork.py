import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Įkeliam Titanic duomenų rinkinį
titanic = sns.load_dataset("titanic")

df = pd.DataFrame(titanic)

# print(df.head())
# print(df.describe())
# print(df.info())

# Išmetam eilučių su trūkstamomis reikšmėmis (supaprastinimui)
df = titanic.dropna(subset=["age", "fare", "sex", "survived"])

# Konvertuojam kategorinius duomenis į skaitinius
df.loc[:, "sex"] = df["sex"].map({"male": 0, "female": 1})


# Pasirenkam bruožus ir taikinį
X = df[["age", "fare", "sex"]] # independent variables (features).
y = df["survived"] # dependent variable (target) – did the passenger survive?

# Duomenų padalijimas // stratify=y ensures both train/test sets have the same proportion of survived/died.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=95)

# Modelio mokymas
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Spėjimai ir vertinimas
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Modelio tikslumas: {accuracy:.2f}")
print("Sumišimo matrica:")
print(conf_matrix)

# Vizualizacija (nebūtina, bet galima):
sns.pairplot(df[["age", "fare", "sex", "survived"]], hue="survived")
# plt.show()


