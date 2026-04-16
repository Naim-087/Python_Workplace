import numpy as np


#np.random.uniform(star,end ,shape)

arr=np.random.rand(2,3) #gives float val 0--->1

print(type(arr))
print(arr.ndim)
print(arr)
print(arr.dtype)
print(arr.shape)
print(arr.size)

#np.random.uniform(star,end ,shape)
arr=np.random.randint(1,10,(4,3)) # every valu range will be 1-10

print(type(arr))
print(arr.ndim)
print(arr)
print(arr.dtype)
print(arr.shape)
print(arr.size)

