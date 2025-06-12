import pandas as pd
import matplotlib.pyplot as plt

"""1"""
df = pd.read_csv('train.csv')
# print(df)

"""2"""
# pd.set_option('display.max_rows', None) # del atvaizdavimo visu eiluciu
# print(df.info()) # spausdinam informacija

# grouped = df.groupby('Age')
# # print(grouped.median(numeric_only=True)) # numeric reikalingas, jeigu yra NaN, kad atsispausdinti
# new_age_df = df['Age'].fillna(df['Age'].median(), inplace=False)  # inplace - Atlik pakeitimą tame pačiame DataFrame, jo nekopijuojant.
# # new_age_df.to_csv('new_age.csv') # uzrasom i csv faila
group_means = df.groupby(['Pclass', 'Sex'])['Age'].mean()

# palei klases ir lyties vidurki, priskiriam amziaus vidurki nuliniai reiksmei.
df['Age'] = df.apply(
    lambda row: group_means.loc[(row['Pclass'], row['Sex'])] if pd.isnull(row['Age']) else row['Age'],
    axis=1
).round(2)
df.to_csv('new_age.csv', index=False)
####################################################################################################
####################################################################################################
####################################################################################################
"""3"""
'''•Sukurkite bendrą stulpelį susumavę brolius seseris ir tėvus,
kad sužinotumėte šeimos dydį, senus stulpelius galite pašalinti (Parch ir SibSp)'''

# parch = df[['Parch', 'SibSp']]
# parch_count = parch.value_counts()
# parch_count.to_csv('parch_count.csv')

# print(age)
# df_name = df['Name'].apply(lambda name: name.split(',')[0])
# df_family_names = df_name.value_counts()
# df_family_names.to_csv('names.csv')


df_exclude = df[~((df['Parch'] == 0) & (df['SibSp'] == 0))] # & == AND, ~ == NOT, | == OR
# print(df_exclude)
# df_exclude.to_csv('remove_singles.csv')
skaiciuojam = df_exclude.value_counts()
# print(skaiciuojam)
# print(parch_count)

dean = df[df['Ticket'] == 'C.A. 2315']
# print(dean)

matching_family = df[
    (df['SibSp'] == 1) &
    (df['Parch'] == 2) &
    (df['Embarked'] == 'S')
]
# print(matching_family)
# matching_family.to_csv('filtered_family_embarked_C.csv', index=False)

'''Final countdown tutututuutut'''
df['LastName'] = df['Name'].apply(lambda name: name.split(',')[0]) # issitraukiam pavardes (iki kablelio pirma reiksme)

df['FamilyID'] = df['LastName'] + '_' + df['Ticket'].astype(str)  # bilietus pasidarom str, nes yra skiritngu tipu bilietu

family_sizes = df['FamilyID'].value_counts()
# print(family_sizes)

df['FamilySize'] = df['FamilyID'].map(family_sizes) # Jei Dean_C.A. 2315 pasikartojo 4 kartus → visi Dean’ai su tuo bilietu gaus FamilySize = 4

df.drop(columns=['SibSp', 'Parch'], inplace=True)
# df.drop(columns=['FamilyID'], inplace=True)

df.to_csv('train_family_size.csv')


'''4'''

df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
# print(df['IsAlone'].value_counts())

df.to_csv('train_family_size.csv')

'''5'''

def age_group(age):
    if pd.isna(age):
        return 'unknown'
    elif age < 18:
        return 'child'
    elif age <= 65:
        return 'adult'
    else:
        return 'senior'

df['AgeGroup'] = df['Age'].apply(age_group)
df.to_csv('train_family_size.csv')

'''6'''
avg_age_per_class = df.groupby('Pclass')['Age'].mean().round(2)
# print(avg_age_per_class)

'''7'''

pay_to_live = df.groupby(['Survived', 'Sex'])['Fare'].mean().round(2)

# print(pay_to_live)

# Paverčiam į DataFrame, kad būtų lengviau vizualizuoti
pay_to_live_df = pay_to_live.unstack() # del multiindekso unstack(). -> paverčia grupuotus duomenis į lengvai braižomą formatą.

# Braižom stulpelinę diagramą
pay_to_live_df.plot(kind='bar', figsize=(8, 5), color=['lightblue', 'lightcoral'])

plt.title('Vidutinė bilieto kaina pagal lytį ir išgyvenimą')
plt.xlabel('Išgyvenimo statusas (0 = neišgyveno, 1 = išgyveno)')
plt.ylabel('Vidutinė bilieto kaina')
plt.legend(title='Lytis')
plt.xticks(ticks=[0, 1], labels=['Neišgyveno', 'Išgyveno'], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
##############################################################################
##############################################################################
##############################################################################
'''PLAYGROUND'''

# df_boys_count = df[(df['AgeGroup'] == 'child') & (df['Survived'] == 1) & (df['Sex'] == 'male')].shape[0]
# print(df_boys_count)

# df_girls_count = df[(df['AgeGroup'] == 'child') & (df['Survived'] == 1) & (df['Sex'] == 'female')].shape[0]
# print(df_girls_count)

# print(df.info())

mean_ages = df.groupby(['Pclass', 'Sex'])['Age'].mean()
print(mean_ages)

# df_missing_ages.to_csv('analyse_survival.csv')

# print(df[['Survived', 'Age', 'Fare', 'Pclass', 'FamilySize']].corr())

df_survival = df[(df['Pclass'] == 2) & (df['Survived'] == 1)]
df.drop(columns=['LastName', 'FamilyID'], inplace=True)

df.to_csv('analyse_survival.csv', index=False)
# print(df_survival)

# kiek kiekviena klase turi nenuliniu reiksmiu palei cabin.
x = df.groupby(['Pclass'])['Cabin'].apply(lambda x: x.notna().sum())
print(x)
