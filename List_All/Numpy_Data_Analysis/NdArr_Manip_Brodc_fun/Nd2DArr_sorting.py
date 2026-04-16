import numpy as np
mat=np.array([[10,3,5],
              [90,55,23]]
              )

#row wise sorting  :  for horizon axis =1

hor_sort= np.sort(mat,axis=1)
print(hor_sort,"\n")

#col wise sorting : for verticle axis = 0

vert_sort=np.sort(mat,axis=0)
print(vert_sort)

