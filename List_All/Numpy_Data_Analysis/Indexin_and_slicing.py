import numpy as np

arr=np.arange( 1, 10,1)
mat=arr.reshape(3,3)
print(mat)
print("indexing")
print([6])
print([9])

"""Slicing"""

#1D =arr[start:end:step]
#2D= arr[row_start : row_end : step , col_start : col_end : step]

"""getting a row"""
row_0=mat[0:1 , ] #row=0,1st row. row=1,2nd row. there is no col range , son defualt all values come
print(row_0)
row_1=mat[1:2 , ]
print(row_1)
row_2=mat[2:3 , ]
print(row_2)
 
print("\ncolumn\n")
col_0=mat[: ,0:1]
print(col_0)

col_1=mat[: ,1:2]
print(col_1)








