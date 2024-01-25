# index, slicing
# iterating through an array
# stacking together arrays
# indexing with boolean arrays

import numpy as np

arr1 = np.array([1,2,3,4])
a = arr1[0]
# 3d
arr2 = np.array([[1,2,3],[3,4,5],[5,6,7]])
# [[1 2 3]
#  [3 4 5]
#  [5 6 7]]

# indexing
# print(arr2)
# row 2: [5,6,7]
# column 1: [2,4,6]
b = arr2[2,1] # output: 6

# slicing
c = arr2[0:2,2]
# rows 0 and 1 [1,2,3,3,4,5]
# column 2: [3,5,7]
# output: [3,5]

# iterate through an array
# for row in arr2:
#     print(row)

# Stacking arrays
# Condition: Arrays must have the same shape
# vertical stacking
arr3 = np.arange(6).reshape(3,2)
arr4 = np.arange(6,12).reshape(3,2)
print(arr3)
# [[0 1]
#  [2 3]
#  [4 5]]
print(arr4)
# [[ 6  7]
#  [ 8  9]
#  [10 11]]
# np.vstack((a,b))
# print(np.vstack((a,b)))
# [[ 0,  1],
#  [ 2,  3],
#  [ 4,  5],
#  [ 6,  7],
#  [ 8,  9],
#  [10, 11]])

# horizontal stack
np.hstack((a,b))
# print(np.hstack((a,b)))
# [[ 0,  1,  6,  7],
# [ 2,  3,  8,  9],
# [ 4,  5, 10, 11]]

# splitting
arr5 = np.arange(12)

# horizontal splitting
hsplit_arr5 = np.hsplit(arr5,6)
# print(hsplit_arr5)
# array([0, 1]), array([2, 3]), array([4, 5]), array([6, 7]), array([8, 9]), array([10, 11])]

# vertical split
# Condition: work on 2D arrays and so on
arr6 = np.array([[1,2],[3,4],[5,6]])
# print(arr6)
# [[1 2]
#  [3 4]
#  [5 6]]
# vsplit_arr6 = np.vsplit(arr6,2)
# print(vsplit_arr6)
# output: [array([[1, 2]]), array([[3, 4]]), array([[5, 6]])]

# indexing with boolean arrays
arr7 = np.arange(12)
greater_than_5 = arr7 > 5
elements = arr7[arr7 > 5]
print(elements)
# output: [ 6  7  8  9 10 11]


