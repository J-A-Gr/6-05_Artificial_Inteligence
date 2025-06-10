import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""ROUND 1"""
# np.random.seed(365)
daily_sales = np.random.randint(50, 500, size = 365)

# print(np.shape(daily_sales))
# print(daily_sales)

"""ROUND 2"""

# dates = np.arange('2025-01-01', '2026-01-01', dtype='datetime64[D]')
dates = pd.date_range(start='2025-01-01', periods=365)
# print(dates)

dates_with_sales = pd.Series(daily_sales, index=dates)
# print(dates_with_sales)

"""ROUND 3"""

# print(dates_with_sales.resample('ME').mean())
# print(dates_with_sales.resample('W').mean())

"""ROUND 4"""

# original_dates_with_sales = dates_with_sales.copy()

# dates_with_sales[dates_with_sales == 100] *= 10
# dates_with_sales[dates_with_sales == 400] /= 400

dates_with_sales.iloc[6] = 1000
dates_with_sales.iloc[199] = -1000
dates_with_sales.iloc[268] = 1000

# num_changed = (dates_with_sales != original_dates_with_sales).sum()
# print("How many values changed:", num_changed)

"""ROUND 5"""

mean = dates_with_sales.mean()
std = dates_with_sales.std()

# 2x standartinis nuokrypis
dvigubas_nuokrypis = 2 * std
# print(mean)
# print(std)
# print(dvigubas_nuokrypis)

# Randame anomalijas
anomalijos = dates_with_sales[np.abs((dates_with_sales - mean)) > dvigubas_nuokrypis] # np.abs nespausdina neigiamu reiksmiu. (neigiamas i teigiama. teigamas-teigiamas, nulis-nulis)

print("Anomalijų datos ir pardavimų kiekiai:")
print(anomalijos)

# plt.figure(figsize=(10,5)) # plotis / aukštis
# plt.plot(dates_with_sales, label='Pardavimai') # Braižo linijinį grafiką | x = datos, y = pardavimu kiekiai
# plt.scatter(anomalijos.index, anomalijos.values, color='red', label='Anomalijos') # Prideda taškų grafiką, x = dienos, y = pardavimai.
# plt.legend() # parodo 'legenda' panaudoja label reiksmes is anksciau.
# plt.title("Dieniniai pardavimai su anomalijomis") # grafiko pavadinimas virsuj
# plt.show()