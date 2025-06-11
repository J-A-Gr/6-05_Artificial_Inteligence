import pandas as pd
import numpy as np

dictionary = {
    "Temperature": [-2, 10, -12, 15, np.nan],
    "Humidity": [70, 65, 80, np.nan, 75],
    "Wind Speed": [5, 7, np.nan, 10, 6],
    "Condition": ["Sunny", "Cloudy", "Rainy", "Sunny", "Windy"],
    "City": ["Vilnius", "Kaunas", "Klaipeda", "Šiauliai", "Panevėžys"]
}

list_of_lists = [
    ['Temperature', 'Humidity', 'Wind Speed', 'Condition', 'City'],
    [-8, 70, 5, 'Sunny', 'Vilnius'],
    [10, 65, 7, 'Cloudy', 'Kaunas'],
    [-12, 80, np.nan, 'Rainy', 'Klaipeda'],
    [15, np.nan, 10, 'Sunny', 'Šiauliai'],
    [np.nan, 75, 6, 'Windy', 'Panevėžys']
    ]

"""1"""
def create_dataframe(data):
    df = pd.DataFrame(data)
    return df

df = create_dataframe(dictionary)
# print(df)

"""2"""
# print(df.loc[[1, 3]])
"""3"""
# print(df.loc[df['Temperature'] < 0])
"""4"""
# print(df['Temperature'].sum())
"""5"""
def add_vejas5(df):
    df['Vėjas'] = [50, 5, 17, 99, 2]
    return df
"""6"""
def persalimo_rizika6(df):
    add_vejas5(df)
    df['Peršalimo rizika'] = 'Ne'
    df.loc[df['Temperature'] < 0, 'Peršalimo rizika'] = 'Taip'
    return df
"""7"""
def vejo_pakeitimas7(df):
    persalimo_rizika6(df)
    df['Vėjas'] = df['Vėjas'].apply(
        lambda x:
          'SILPNAS' if x < 10 else 
          ('VIDUTINIS' if x <= 20 else 'STIPRUS')
    )
    return df
"""8"""
def grupuojam_rizika8(df):
    vejo_pakeitimas7(df)
    grouped = df.groupby('Peršalimo rizika')['Temperature'].mean()
    print(grouped)
"""9"""
def rikiavimas_temperaturos9(df):
    vejo_pakeitimas7(df)
    sort = df.sort_values('Temperature', ascending = False)
    print(sort)
"""10"""
def sujungiame_duomenis10():
    # Sukuriame pirmą DataFrame su datomis ir temperatūromis
    df_temp = pd.DataFrame({
        "Data": ["2025-06-08", "2025-06-09", "2025-06-10"],
        "Temperatūra": [30, 34, 29]
    })

    # Sukuriame antrą DataFrame su datomis ir vėjo stiprumu
    df_vejas = pd.DataFrame({
        "Data": ["2025-06-08", "2025-06-09", "2025-06-10"],
        "Vėjas": [11, 22, 39]
    })

    # Sujungiame juos pagal stulpelį "Data"
    df_sujungtas = pd.merge(df_temp, df_vejas, on="Data")

    return df_sujungtas

print(sujungiame_duomenis10())