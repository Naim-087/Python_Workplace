import numpy as np

dict= { 'a' :10,
        'b' :20,
        'c':30,
        'd':40
}

arr=np.array(dict)

print(type(arr))
print(arr.dtype)
print(arr.shape)
print(arr.size)
print(arr)
