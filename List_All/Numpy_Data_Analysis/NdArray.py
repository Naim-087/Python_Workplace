import numpy as np 
#1D array
arr1 = np.array([1,2,3,4,5])
print(type(arr1))


#2d array
arr2= np.array(   [ [1,2,3,4], #row1
                    [4,5,6,7] #row2
                  ])

print(arr1.ndim)
print(arr2.ndim)

#shape
print(arr1.shape)
print(arr2.shape)

#data type
print(arr1.dtype)
print(arr2.dtype)

#size
print(arr1.size)
print(arr2.size)


