import numpy as np

#sorting without copying
y=np.array([ 70, 14, 33, 29, 17])

z=y.copy()

print(z)
z.sort()
print(z)
print("check does y exis now =",y)
#with copying and remaini man array

sort_arr=np.sort(y)

print(sort_arr)
print("check does y exis now =",y)

