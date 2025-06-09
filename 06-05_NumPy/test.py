# rows = 6

# for i in range(rows):
#     for j in range(i):
#         # If the sum of row index and column index is even, print 1; else, print 0
#         print((i + j) % 2, end=' ')
#     print()

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

jungiames = np.concatenate((b,a))

print(jungiames)

naujas_array = jungiames.reshape(2,4)
print(naujas_array)

# test_array = np.linspace(2, 5)
# print(test_array)


"""
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""