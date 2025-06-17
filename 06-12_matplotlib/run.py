import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Nustatome stilių
sns.set(style="darkgrid")

# Įkeliame duomenis
df = pd.read_csv("analyse_survival.csv")  

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

# Sukuriame amžiaus grupes
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80], right=False)

# Grupavimas: amžiaus grupė + lytis → vidutinė išgyvenamumo reikšmė (t. y. tikimybė)
survival_table = df.groupby(['AgeGroup', 'Sex'])['Survived'].mean().unstack()

# Apvaliname iki 2 skaitmenų
survival_table = survival_table.round(2)

# Vizualizuojame heatmap'u
plt.figure(figsize=(8, 6))
sns.heatmap(survival_table, annot=True, fmt=".2f", cmap="YlGnBu")
plt.title("Išgyvenamumo tikimybė pagal amžių ir lytį")
plt.xlabel("Lytis")
plt.ylabel("Amžiaus grupė")
plt.tight_layout()
plt.show()



