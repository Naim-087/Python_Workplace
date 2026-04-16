import numpy as np
#taking a 3D array
"""
shape of 3d array :
(ddepth, rows , columns), depth =2[3d]

"""
matrix=[ [[1, 2, 3], [4, 5, 6]], 
        [[7, 8, 9], [10, 11, 12]]
    ]
arr=np.array(matrix)
print(arr)
print(arr.shape)
print("depth,rows,columns")
print("\n\n")
#np.zeros
arr1=np.zeros((3,3,3),dtype=np.int64) #row X col


print(type(arr1))
print(arr1.ndim)
print(arr1)
print(arr1.dtype)
print(arr1.shape)
print(arr1.size)

#np.ones like first 3d array
print("\n\n")
arr=np.ones_like(arr)
print(arr)

#np.ones
arr3=np.ones((2,3),dtype = np.int32)
print(arr3)
print(arr3.shape)
print(arr3.size)








