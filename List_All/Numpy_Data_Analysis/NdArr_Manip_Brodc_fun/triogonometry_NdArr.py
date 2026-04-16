import numpy as np

x= np.array([10,20,30,40,50])

sin_val=np.sin(x)
"""takes val on rad"""
print("sin_val = ",sin_val)
print("cos_val = ",np.cos(x)) 

"""red to degree conv"""

deg_con=np.rad2deg(x)
print(deg_con)


