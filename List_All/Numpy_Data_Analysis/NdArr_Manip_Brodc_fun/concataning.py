import numpy as np

a=np.random.randint(1 , 10,size=(2,3)) #row x col # sample x feature
b=np.random.randint(20 , 30,size=(2,3))
print(a,"\n")
print(b)

con_row = np.concatenate((a,b),axis=0) #row wise
print("\n",con_row,"\n")

con_col = np.concatenate((a,b),axis=1) #col wise
print(con_col)


