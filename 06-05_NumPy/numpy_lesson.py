import time
import numpy as np

# numpy masyvo kūrimas
my_array = np.array(
    [
        [1,2,3],
        [7,8,9]
    ]
    ) 
 
print(my_array)

for i in my_array.transpose():

    print(i)

print(my_array.shape)


                    # shape struktūra
# zeros_arr = np.zeros((3, 5))
# print(zeros_arr)


initial = list(range(0,10000000))

# python list
my_list = initial
start = time.time()

python_res = [x*2 for x in my_list]

python_time = time.time() - start

# numpy list
numpy_arr = np.array(initial)
start = time.time()

numpy_res = numpy_arr * 2

numpy_time = time.time() - start

print(f"Python: {python_time:.4f} s")
print(f"Numpy: {numpy_time:.4f} s")