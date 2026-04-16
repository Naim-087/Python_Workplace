import numpy as np

x=np.array([ 10, 8, 33, 43, 21])
y=np.array([ 13, 14, 33, 29, 17])

greater_than = x>y
print(greater_than)

equal = x==y
print(equal)

not_eq= x!=y
print(not_eq)
 #all() -> return true if all true
 #any() -> return true atleast one is true

print(np.all(greater_than))
print(np.any(greater_than))


