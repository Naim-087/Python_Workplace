import numpy as np
mat=np.array([[10,3,5],
              [90,55,23]]
              )

max_val=np.argmax(mat) #return index
print(max_val)

"""
np.argmax(mat) flattens the matrix into a 1D array internally:
[10, 3, 5, 90, 55, 23]
"""

min_val=np.argmin(mat) #return index
print(min_val)




