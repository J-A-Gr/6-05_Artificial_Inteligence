import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Nustatome stilių
sns.set(style="darkgrid")

# Įkeliame duomenis
df = pd.read_csv("analyse_survival.csv")  # naudok savo kelią, jei reikia

# 1. Keleivių kiekis kiekvienoje klasėje
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Pclass', palette='Set2')
plt.title('Keleivių kiekis kiekvienoje klasėje')
plt.xlabel('Klasė')
plt.ylabel('Keleivių skaičius')
plt.tight_layout()
plt.show()

# 2. Išgyvenamumas pagal lytį ir klasę
sns.catplot(data=df, x="Pclass", hue="Sex", col="Survived", kind="count", palette="Set1")
plt.subplots_adjust(top=0.8)
plt.suptitle('Išgyvenamumas pagal lytį ir klasę')
plt.show()

# 3. Klasių pasiskirstymas pagal amžių
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", hue="Pclass", multiple="stack", palette="Set2", bins=30)
plt.title('Klasių pasiskirstymas pagal amžių')
plt.xlabel('Amžius')
plt.ylabel('Keleivių skaičius')
plt.tight_layout()
plt.show()

# 4. Išgyvenamumas pagal amžių
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Age", hue="Survived", multiple="stack", palette="Set1", bins=30)
plt.title('Išgyvenamumas pagal amžių')
plt.xlabel('Amžius')
plt.ylabel('Keleivių skaičius')
plt.tight_layout()
plt.show()

# 5. Koreliacija tarp skaitinių kintamųjų
plt.figure(figsize=(10, 8))
numeric_corr = df.select_dtypes(include='number').corr()
sns.heatmap(numeric_corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title('Skaitinių kintamųjų koreliacijos matrica')
plt.tight_layout()
plt.show()

# 6. Išgyvenamumas pagal amžių ir lytį
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Age", hue="Sex", multiple="dodge", bins=30, palette="Set1", stat="count")
plt.title("Išgyvenamumas pagal amžių ir lytį")
plt.xlabel("Amžius")
plt.ylabel("Keleivių skaičius")
plt.tight_layout()
plt.show()
