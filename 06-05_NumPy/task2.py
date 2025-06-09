import numpy as np
from matplotlib import pyplot as plt

# 2024-01-01 iki 2024-12-31
dates = np.arange('2024-01-01', '2025-01-01', dtype='datetime64[D]') # dtype, (dienos tikslumu[d])
days_per_month = np.array([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
month_ids = np.repeat(np.arange(12), days_per_month) # .repeat išplečia kiekvieną mėnesio indeksą tiek kartų, kiek yra to mėnesio dienų

# min/max temperatūros
monthly_ranges = np.array([
    [-21,  11], [-2, 10], [-5, 15], [0, 19], [-3, 23], [15, 35],
    [21, 40], [17, 43], [10, 22], [5, 15], [-23, -43], [-5, -40]
])

# Išgaunam kiekvieno mėnesio min ir max reikšmes per indeksus
min_temps = monthly_ranges[month_ids, 0]
max_temps = monthly_ranges[month_ids, 1]

# Generuojam atsitiktines temperatūras pagal ribas
np.random.seed(0) # jeigu norima, kad kas kart butu tie patys rezultatai (test purpose)
temps = np.random.uniform(low=min_temps, high=max_temps) # sugeeruojam vienu kartu reiksmes min/max

########################################################################

# Į kiekvieną mėnesį įdedam po 2 anomalijas
for m in range(12):
    idx = np.where(month_ids == m)[0]  # dienų indeksai tam mėnesiui
    # Šiluminė anomalija
    high_idx = np.random.choice(idx)
    temps[high_idx] = max_temps[high_idx] + np.random.uniform(10, 20)
    # Šalčio anomalija
    low_idx = np.random.choice(idx)
    temps[low_idx] = min_temps[low_idx] - np.random.uniform(10, 20)

########################################################################

# Suskaičiuojam vidurkius kiekvienam mėnesiui 
monthly_avg_temps = np.array([temps[month_ids == m].mean() for m in range(12)])  # temps[month_ids == m] grąžina visas to mėnesio temperatūras.

# Atspausdinam
for m, avg in enumerate(monthly_avg_temps, start=1):
    print(f"{m:02d} mėn. vidutinė temperatūra: {avg:.2f}°C")

########################################################################

mean = temps.mean()
std = temps.std()

# Anomalija = daugiau nei 2 std nuo vidurkio
anomaly_mask = (temps > mean + 2 * std) | (temps < mean - 2 * std)
anomaly_indices = np.where(anomaly_mask)[0]

# Atspausdinam
print("\nAnomalijos:")
for i in anomaly_indices:
    print(f"{dates[i]}: {temps[i]:.2f}°C")

plt.scatter(np.arange(1, 13), monthly_avg_temps)
plt.xlabel("Mėnuo")
plt.ylabel("Vidutinė temperatūra (°C)")
plt.title("Vidutinė mėnesio temperatūra per 2024 metus")
plt.grid(True)
plt.show()