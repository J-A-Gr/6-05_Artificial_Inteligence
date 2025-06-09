import numpy as np

kainos = np.array([3.50, 7.99, 2.99, 12.50, 5.00])

bendra_suma = np.sum(kainos)
print(f"Bendra suma: {bendra_suma} €")

vidurkis = np.mean(kainos)
print(f"Vidutinė kaina: {vidurkis:.2f} €")

kainos_su_mokesciu = kainos * 1.10
print("Kainos su 10% mokesčių:", kainos_su_mokesciu)
