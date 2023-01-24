import pandas as pd
import numpy as np

cars = pd.read_csv("Python_code\\PrinciplesOfDS_Course\\Labs\\Data\\cars.csv")

print(cars.columns)

# y is the 'ground truth value' in this calss.. not the prediction value. 
# he said the prediction value is Xw... where X is the feature matrix.. and a min-2-norm equation involving the ground truth value and prediction value is important too... 
# 'w' is the model parameter .. 

print(cars.MPG)
mpg1 = cars.MPG[:6].to_numpy()
mpg2 = cars.MPG[6:12].to_numpy()
print(mpg1, mpg2, type(mpg1))

mpgCombine = mpg1 + mpg2
print(mpgCombine, type(mpgCombine)) # unequal length arrays cannot be added 

numberMat = cars[[ 'MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration']]
print(numberMat) 

# there is a np.outer() func... also np.multiply() ... not totally sure about diffs rn.. maybe find an article or start throwing things into each 

npNumM = numberMat.to_numpy()
# numMat2 = npNumM.outer(npNumM)
# numMat3 = npNumM.multiply(npNumM) # error... 

# print(numMat2)
# print(numMat3)
print(npNumM)
print(np.multiply(npNumM,npNumM)) # works for matrix elementwise multiplication of 2 matrices 

# Sparse model is one in which many elements within the model will become 0 when calculated.. 
# different norms allow one to see what effects each feature might have on ones data by revealing which ones are contributing most to a given predictive model... he is saying th l1 norm helps select / identify important features. 

# NORMS 
print("mpg1:",mpg1)
print("ord=1:",np.linalg.norm(mpg1, ord=1)) # 99.0
print("ord=2:",np.linalg.norm(mpg1, ord=2)) # 40.534
print("ord=np.inf:",np.linalg.norm(mpg1, ord=np.inf)) # 18.0 ... this one makes sense.. but the l1 norm doesnt... hm.. maybe it summed the vec? 
print("ord='fro':",np.linalg.norm(npNumM, ord='fro')) # 62608.42403774431

val = 18+15+18+16+17+15
print(val) # 99 ... yes a sum indeed 











