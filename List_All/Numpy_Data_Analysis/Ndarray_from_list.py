#list
import numpy  as np 

lst=[10,20,30,40,50]

arr=np.array(lst)
print(type(arr))
print(arr.ndim)

#mixed list
lst=[10,20.5,30,"mixed list",50]
arr=np.array(lst)
print(type(arr))
print(arr.ndim)
print(arr.dtype)

#matrix
matrix=   [ [1,2,3,4], #row1
            [4,5,6,7] #row2
    
    ]
arr= np.array(matrix)

print(arr.shape)

print(arr.ndim)
print(arr.dtype)
