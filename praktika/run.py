import numpy as np

""" 📘 1. Sukurk NumPy masyvą nuo 0 iki 9"""

# naujas_array = np.arange(10)
# print(naujas_array)

"""  2. Sukurk 3x3 masyvą tik su nuliais
 Tikslas: praktikuoti np.zeros()."""

# new_array = np.zeros((3,3))
# print(new_array)

"""📘 3. Sukurk 5 skaičių masyvą nuo 10 iki 50
Tikslas: naudoti np.arange()."""

# new_array = np.arange(10, 51, 10)
# print(new_array)

"""📘 4. Sukurk 3x3 vienetų (1) matricą
Tikslas: naudoti np.ones()."""

# new_array = np.ones((3,3))
# print(new_array)

""" 5. Sukurk 5 skaičių masyvą su atsitiktiniais skaičiais tarp 0 ir 1
Tikslas: naudoti np.random.rand()."""

# new_array = np.random.rand(5)
# print(new_array)

"""📘 6. Sukurk 10 sveikų atsitiktinių skaičių nuo 1 iki 100
Tikslas: naudoti np.random.randint()."""

# new_array = np.random.randint(101, size=10)
# print(new_array)

"""📘 7. Apskaičiuok vidurkį ir sumą iš masyvo"""

# arr = np.array([1, 2, 3, 4, 5])

# mean_array = np.mean(arr)
# sum_array = np.sum(arr)
# print(mean_array, sum_array)

"""📘 8. Pakeisk visus masyvo elementus, kurie yra didesni nei 5, į 0"""

arr = np.array([2, 6, 1, 8, 4])
arr[arr > 5] = 0
print(arr)

"""📘 9. Sukurk 3x3 matricą su skaičiais nuo 1 iki 9 ir ištrauk antrą eilutę"""

# new_arr = [[1,2,3],[4,5,6],[7,8,9]]
# arr = np.array(new_arr)
# print(arr[1, :])
# print()
# print(arr)

""" 10. Ištrauk kampinius elementus iš 3x3 matricos"""

# print(arr[0:, 0])
# print(arr[0, 0:])