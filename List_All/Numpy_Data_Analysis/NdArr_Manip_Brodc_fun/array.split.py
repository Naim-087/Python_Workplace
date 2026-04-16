import numpy as np

 
mat=np.random.randint(20 , 30,size=(10,))
print(mat,"\n")

splitted_array= np.array_split(mat,3)

print(splitted_array)
