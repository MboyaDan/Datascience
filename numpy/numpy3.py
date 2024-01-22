# iterating through a numpy array
import numpy as np

arr1 = np.array([[1,3],[4,5],[7,8]])
arr2 = np.array([[11,12],[13,14],[15,16]])
print(arr1)

# [[1 3]
#  [4 5]
#  [7 8]]

# for loop
for x in arr1:
    print(x)

# result
# [1 3]
# [4 5]
# [7 8]

# nditer
# iterating row wise
for x in np.nditer(arr1,order="C"):
    print(x)

# result:
    
# 1
# 3
# 4
# 5
# 7
# 8

# # iterating column wise
for x in np.nditer(arr1,order="F"):
    print(x)
# result: 
    
# 1
# 4
# 7
# 3
# 5
# 8
    
# print two array simultaneously
for x,y in np.nditer([arr1,arr2]):
    print(x,y)

# result:
    
# 1 11
# 3 12
# 4 13
# 5 14
# 7 15
# 8 16
    

