import numpy as np

x= np.array([ 10 , 20 , 30 , 40 ])
#sqr for each element

result= x**2 
print(result,"\n")

#add with result
result = x+3
print(result,"\n")

matrix = np.array([[10,20,30],
                  [90,6,44]
                  ])

result= matrix-3
print(result,"\n")

#vector

vector = np.array([1,2,3])

result=matrix + vector
print(result)

