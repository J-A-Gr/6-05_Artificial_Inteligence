import numpy as np

"""[1] 1D masyvas"""
# masyvas_array = np.array([1, 2, 3, 4, 5])
# arranged_list = np.arange(1,6)
# print(masyvas_array)
# print(arranged_list)

"""[2] 2D masyvas"""

# masyvas_2_array = np.zeros([3,3])
# print(masyvas_2_array)

"""[3] masyvas, masyve = lentele(matrica) su eilutemis ir stulpeliais"""

# sarasas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrica = np.array(sarasas)
# print(matrica)
# print(f"*" * 20)

# print(matrica[0, 1]) # pirma eilutė, antras stulpelis

# print(f"*" * 20)
# sliced_matrica = matrica[0:2, 1:3]
# print(sliced_matrica)

"""[4]"""

pirmas_masyvas = np.array([1, 2, 3])
antras_masyvas = np.array([4, 5, 6])
naujas_masyvas = []
####################################################
"""sudėtis"""

# for i in range(len(pirmas_masyvas)):
#     naujas_masyvas.append(pirmas_masyvas[i] + antras_masyvas[i])
# print(naujas_masyvas)

# tuscias = []
# for i in naujas_masyvas:
#     tuscias.append(int(i))
# print(tuscias)

# paverstas_masyvas = [int(i) for i in naujas_masyvas]
# print(paverstas_masyvas)

####################################################
"""atimtis"""
# atimtis_1 = np.subtract.reduce(pirmas_masyvas)
# print(atimtis_1)

# atimtis_2 = np.subtract.reduce(antras_masyvas)
# print(atimtis_2)

# for i in range(len(pirmas_masyvas)):
#     naujas_masyvas.append(pirmas_masyvas[i] - antras_masyvas[i])
# print(naujas_masyvas)

# pavertimas_int = [int(x) for x in naujas_masyvas] # pasivert sarasa i int, kad nebutu np.int64
# print(pavertimas_int)
####################################################
"""daugyba"""

# daugyba_masyvu = np.multiply(pirmas_masyvas, antras_masyvas)
# print(daugyba_masyvu)

# result = 1 # is nulio nesidaugina :)

# for i in pirmas_masyvas:
#     result *= i
# print(result)


"""dalyba"""

# dalyba_masyvu = np.divide(pirmas_masyvas, antras_masyvas)
# print(dalyba_masyvu)

# result = antras_masyvas[0] 

# for i in antras_masyvas[1:]:
#     result /= i

# print(result)
####################################################
"""suma"""

# sum_result_pirmas = np.sum(pirmas_masyvas)
# print(sum_result_pirmas)
# sum_result_antras = np.sum(antras_masyvas)
# print(sum_result_antras)
####################################################
"""vidurkis"""

# mean_result_pirmas = np.mean(pirmas_masyvas)
# print(mean_result_pirmas)
# mean_result_antras = np.mean(antras_masyvas)
# print(mean_result_antras)
####################################################
"""maksimumas"""

# max_result_pirmas = np.max(pirmas_masyvas)
# print(max_result_pirmas)
# max_result_antras = np.max(antras_masyvas)
# print(max_result_antras)

####################################################
"""minimumas"""


# min_result_pirmas = np.min(pirmas_masyvas)
# print(min_result_pirmas)
# min_result_antras = np.min(antras_masyvas)
# print(min_result_antras)

########################################################################################################
"""pi masyvai, trigonometrines func [sin, cos, tan]"""
# my_arr = np.array([0, np.pi/2, np.pi])
# print(my_arr)

# sinus = np.sin(my_arr)
# print(sinus)

# cos = np.cos(my_arr)
# print(cos)

# tan = np.tan(my_arr)
# print(tan)

####################################################
"""eksponentes ir naturalus logoritmai"""

# exp_values = np.exp(my_arr)
# print(exp_values)

# log_values = np.log(my_arr)
# print(log_values)

# log10_values = np.log10(my_arr)
# print(log10_values)
####################################################
"""random"""

# random_list = np.random.random((3,3))
# print(f"Originalus masyvas \n{random_list}")

# dvigubas_list = random_list * 2
# print(f"Padvigubintas \n{dvigubas_list}")


