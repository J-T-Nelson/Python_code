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
print(npNumM.data) # <memory at 0x000001FC88309E50>
print(npNumM.ndim) # 2
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


A = np.array([[1,2,3], [2,4,5], [5,6,7]])
print("ord='fro' for A :",np.linalg.norm(A, ord='fro'))


B = np.full((3,3), 2)
print(B)

spaced = np.linspace(0,20,5)
print(spaced)

print("info on cars: \n",cars.info())
print("description of cars: \n",cars.describe())

import matplotlib.pyplot as plt

# cars.hist(bins=50, figsize=(20,15))
# plt.show()

# plt.plot(cars['Cylinders'])
# plt.show()

# plt.hist(cars['Horsepower'],bins=50)
# plt.show() # showing multiple plots requires exiting one to view the next right now .... 
# plt.boxplot(cars['Acceleration'])
# plt.show()

# plt.boxplot(cars['Acceleration'], vert=True)
# plt.show()

# plt.scatter(cars['Cylinders'], cars['MPG'])
# plt.show()

# plt.scatter(cars['Cylinders'], cars['Acceleration'])
# plt.show()

####### NOT SURE HOW TO REPRODUCE THE CORRELATION DIAGRAM LIKE IN THE SLIDE ppt4
#hcorr = cars.corr()
#hcorr.style.background_gradient()
#hcorr.show()

# categorical feature inspection 

print(cars.columns)
print(cars['Origin'].value_counts())
#print(cars['Model'].value_counts())

#print(cars.isnull()) # returns boolean matrix
print(cars.isnull().sum()) # returns num missing values by col ... very nice and concise 
print('DF.shape[0] ==', cars.shape[0]) # gets the # of rows in the first col? 





