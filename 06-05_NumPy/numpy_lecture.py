
# Numpy masyvų kūrimas
import time
import numpy as np


# my_array = np.array(
#     [
#         [1,2,3], 
#         [7,8,9]
#     ]
#      )

# # print(my_array)
# print("-" * 20)

# print(my_array.shape)

# trasposed_arr = my_array.transpose()
# print(trasposed_arr.shape)

# for i in trasposed_arr:

#     print(i)

#     # for j in i:
#     #     print(j)
#     # print(i[2])


# print("-" * 20)
# zeros_arr = np.zeros((2,3))
# print(zeros_arr)

# print("-" * 20)
# ones_arr = np.ones((2,3))
# print(ones_arr)

# print("-" * 20)
# arange_arr = np.arange(0,10)
# print(arange_arr)

# print("-" * 20)
# rand_arr = np.random.randint(50,100,(2,3))
# rand_arr = np.random.random((2,3))
# print(rand_arr)

# initial = list(range(0,10000000))

# #Python list
# my_list = initial
# start = time.time()

# python_res = [x * 2 for x in my_list]

# python_time = time.time() - start


# #Numpy list
# numpy_arr = np.array(initial)
# start = time.time()

# numpy_res = numpy_arr * 2

# numpy_time = time.time() - start

# print(f"Python: {python_time:.4f} s" )
# print(f"Numpy: {numpy_time:.4f} s" )
# print(f"NUmpy faster: {python_time/numpy_time:.1f} x" )\



# my_arr = np.array([1,23,6,45,23,0,5,58585,561,56,151,561,561,561,561,561,561,561])

# sum = my_arr.sum()
# print(sum)
# avg = my_arr.mean()
# print(avg)
# min = my_arr.min()
# print(min)
# max = my_arr.max()
# print(max)

# print(my_arr.shape)

# print(my_arr.reshape((2,9)))
# print("-"*20)
# print(my_arr.reshape((3,6)))
# print("-"*20)
# print(my_arr.reshape((9,2)))
# print("-"*20)
# print(my_arr.reshape((6,3)))

# print("-"*20)
# print(my_arr.reshape((3,2,3)))
# print("-"*20)
# complex_arr = my_arr.reshape((6,1,3))
# print(complex_arr)
# print("/"*20)
# simple_arr = complex_arr.reshape((18,))
# print(simple_arr)



# my_arr = np.array([256566514,5,4])

# print(my_arr)
# print(my_arr.dtype)

# my_arr = np.eye(5)

# print(my_arr)


# my_arr = np.ones((3,3))

# # my_arr[0,0] = 0
# # my_arr[1,0] = 0
# # my_arr[2,0] = 0


# print(my_arr[1,0])
# print(my_arr[1,1])

# print(len(my_arr[0]))

# for i in range(len(my_arr[0])):
#     my_arr[i,0] = 0


# print(my_arr)

# np.random.seed(0)

# my_arr = np.random.randint(0,2,(10,10))
# print(my_arr)

# sliced_arr = my_arr[3:7,3:7]

# print(sliced_arr)
# print("-"*20)

# sliced_arr[1,2] = 3

# boolean_arr = sliced_arr[sliced_arr > 0]

# print(boolean_arr)

# my_attendence = np.array([0,1,0,1,1,1])
# my_students = np.array(["Rokas", "Vardenis", "Rokeris", "Rokas K", "Vardenis J", "Rokeris L"])


# for i in range(len(my_attendence)):
#     print(f"{my_students[i]} - {my_attendence[i]}")



my_arr = np.array([0, np.pi/2, np.pi])


sinus = np.sin(my_arr)

print(my_arr)
print(sinus)


exp = np.exp([-1, 0, 1])

print(exp)

mean = np.mean([-1, 0, 1])

print(mean)

std = np.std([-1, 0, 1])

print(std)


# 0.00000000000000012246468


# print(f"{np.pi:.100f}")

# print(type(np.pi))
# print(len(str("141592653589793115997963468544185161590576171875")))