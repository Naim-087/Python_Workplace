import numpy as np

#np.arrange(start.end,step) -> similar to range
arr= np.arange(20 , 30,1)


print(type(arr))
print(arr.ndim)
print(arr)
print(arr.shape)
print("\n\n")

#Create matrix with arrange value
#make a matrix that contains even value from 20-40

array=np.arange(20 , 40,2)
mat=array.reshape(2,5)
print(mat)

