import numpy as np
mat=np.array([[10,3,5],
              [90,55,23]]
              )

#np.where(condition,x,y) if condition is true keep x, otherwise replace with y

index=np.where(mat==55)
print(index,"\n") #1,1 means pos of 55 in mat

index=np.where(mat>3)
print(index,"\n")
"""Elements greater than 3 are located at:
(0,0) → 10
(0,2) → 5
(1,0) → 90
(1,1) → 55
(1,2) → 23"""
##np.where(condition,x,y) if condition is true keep x, otherwise replace with y
index_val= np.where(mat>8,mat,0)
print(index_val)

