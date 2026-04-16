import numpy as np
a= np.random.randint(1,20,size=(100,))
print(a,"\n")


b=np.random.randint(1,100,size=(100,))
print(b,"\n")

val_greater_than_60= np.count_nonzero(b>40) 
#how many val does exist on this data set grtr than 60

print(val_greater_than_60)
#unique valueeeeeees
uni_val = np.unique(b)
print(uni_val)
#with uniq and duplicate value
uni_dup = np.unique(b,return_counts=True)
print(uni_dup)


