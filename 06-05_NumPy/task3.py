import numpy as np

rezultatai = np.array([
    [12, 12, 9, 15],   # Žaidėjas 1
    [8, 15, 14, 10],   # Žaidėjas 2
    [7, 5, 8, 12],     # Žaidėjas 3
    [15, 2, 23, 16],  # Žaidėjas 4
    [12, 10, 11, 9]    # Žaidėjas 5
])

# print(rezultatai)

# suma_rezultato = np.sum(rezultatai)
# print(suma_rezultato)

# vidurkis_rezultato = np.mean(rezultatai)
# print(vidurkis_rezultato)

max_taskai = 0
zaidejas_nr = 0

for i, rez in enumerate(rezultatai):
    taskai = np.sum(rez)
    print(f"{[i + 1]}Žaidėjo rezultas: {taskai}")

    if taskai > max_taskai:
        max_taskai = taskai
        zaidejas_nr = i + 1  

print(f"Daugiausiai taškų surinko žaidėjas {zaidejas_nr} su {max_taskai} taškais.")

geriausias_rez = np.max(rezultatai)
print(geriausias_rez)
