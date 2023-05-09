# Spce to practice fundamentals: 

######-----  -----####################################### 
# setting up normally distributed values in a matrix 
import numpy as np
from scipy import stats
import pandas as pd

M1 = np.random.normal(size=(10,5))
print(M1)

M2 = np.random.normal(loc=0, scale=10, size=(10,5))
print(M2)

M3 = np.random.normal(loc=0, scale=8, size=(10,5))
print(M3)

M4 = np.random.normal(loc=20, scale=5, size=(10,5))
print(M4)

print([stats.describe(mat) for mat in [M1, M2, M3, M4]])
print([pd.DataFrame(mat).describe() for mat in [M1, M2, M3, M4]], end='\n\n') # nice

######-----  -----####################################### 
































             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             