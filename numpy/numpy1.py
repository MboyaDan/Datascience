# pip install numpy

import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Example 3D array
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Accessing elements
print(arr_1d[2])       # Output: 3
print(arr_2d[1, 2])     # Output: 6

# Performing operations
result = arr_1d + 10
print(result)          # Output: [11, 12, 13, 14, 15]