import numpy as np

arr=np.random.randint(1,100,size=(10,5)) #row x col # sample x feature
print(arr.shape)
print(arr,"\n\n")
b=arr.reshape(5,10)
print(b)
print(b.ndim)

#change dimension from 2d to 1d

flatten=b.flatten()
print(flatten)
print(flatten.ndim)

