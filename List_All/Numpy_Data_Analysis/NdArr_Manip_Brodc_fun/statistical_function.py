import numpy as np
a= np.random.randint(20,80,size=(100,))
print(a,"\n")

mean_value = np.mean(a)
print("Mean:", mean_value)

median_value = np.median(a)
print("Median:", median_value)

std_value = np.std(a)
print("Standard Deviation:", std_value)

var_value = np.var(a)
print("Variance:", var_value)


