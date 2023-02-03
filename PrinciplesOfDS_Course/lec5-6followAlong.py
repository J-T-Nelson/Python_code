from cmath import exp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import sys
import os
#print(sys.path) # seeing path variables... not totally sure what they're connected to within python 
print(os.getcwd())


houses = pd.read_csv("../Python_code/PrinciplesOfDS_Course/KaggleWork/KaggleData/melb_data.csv") # working dir is /R_projects ... so going up a dir 

# basic data inspection: 

print(houses.columns, "\n")
print("Shape:",houses.shape)
print(houses.describe())

# I want to separate out just the numeric values within this matrix... Need to understand the classes of each 
print(houses.dtypes)
nonNumericCols = houses.select_dtypes('object')
print(nonNumericCols.dtypes)
print(nonNumericCols)

numericCols = houses.select_dtypes(exclude='object')
print(numericCols.dtypes)
print(numericCols)

# we have separated out numeric from non-numeric cols... now lets check for empty values 
print(numericCols.isnull().sum())
# Rooms               0
# Price               0
# Distance            0
# Postcode            0
# Bedroom2            0
# Bathroom            0
# Car                62
# Landsize            0
# BuildingArea     6450
# YearBuilt        5375
# Lattitude           0
# Longtitude          0
# Propertycount       0
print(numericCols.isnull().sum()/numericCols.shape[0]) # seeing missing vals by percentage
print(numericCols.shape[0]) # this is the number of rows in col 1 I think... 
#print("shape[3]",numericCols.shape[3]) # produces an error... why?   #IndexError: tuple index out of range
 # ^^ produces an error because shape just returns a tuple containing rows x cols x third dim ... etc ... so shape[0] is referencing the rows entry 



# Some cols obviously would be good to omit, some not sure the best way to handle the car col, where a small number of rows is problematic 

numColClean = numericCols.drop(columns=["Car", 'BuildingArea','YearBuilt']) # need to supply the columns arg here... passing a list doesn't apply to columns by default 
print(numColClean.columns)
#Index(['Rooms', 'Price', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude', 'Propertycount'], dtype='object')

import seaborn as sns
corrs = numColClean.corr()
print(type(corrs)) # <class 'pandas.core.frame.DataFrame'>
print(corrs) # its just a data frame containing the correlation values. 

# sns.heatmap(corrs)
# plt.show() # looks decent, somewhat difficult to interpret right now with just colors.. 

# print(help(sns.heatmap)) # bit annoying to get help this way
#sns.heatmap(corrs, annot=True, cmap='coolwarm') # these settings are a little more digestible since numbers are included.. increasing the scale would be nice though 
#plt.show()

# attempting to increase the scale of the heatmap: 
fig, ax = plt.subplots(figsize=(10,10))
hm = ax.matshow(corrs, cmap ='RdBu')

# plt.show() # this is most definitely larger.. but it seems the heatmap was produced with different plotting all together... I don't honestly follow how this was achieved. 
# also this heatmap is largely unlabeled right now 

# filling missing values for Car.. 

numColC2 = numericCols.drop(columns=['BuildingArea','YearBuilt'])
print('Car b4: ', numColC2['Car'].isnull().sum()/numColC2.shape[0]) # Car b4:  0.004565537555228277

numColC2['Car'] = numColC2['Car'].fillna(numColC2['Car'].median())
print('Car After: ', numColC2['Car'].isnull().sum()/numColC2.shape[0]) # Car After:  0.0

# data is looking pretty good now... would be good to visualize some features to understand better now. 
# I would also like to attempt to factorize categorical data for some type of visual inspection as well.. or at least find some means of exploring the non-numeric data

#plt.hist(numColC2['Rooms']) # without additional arguments this produces a stupid looking line... hm 
#plt.hist(numColC2['Rooms'].values) # still a stupid line... what does values do differently than just referencing the col? 
#plt.hist(numColC2['Rooms'].values, 100) # still a line .. this is the code of prof... maybe Rooms is a bad selection is all. 

print("w/o values", numColC2['Rooms'], type(numColC2['Rooms'])) # prints indices next to values within
# Name: Rooms, Length: 13580, dtype: int64 <class 'pandas.core.series.Series'>
print("w/ values:", numColC2['Rooms'].values, type(numColC2['Rooms'].values)) # prints values as a list-like structure
# <class 'numpy.ndarray'>

#plt.hist(numColC2['Rooms'].values, bins=10) # still a line... hmm wonder what is wrong here.. there is definitely data which should fit into a histogram here. 
numColC2.hist(column='Rooms') # this worked... so maybe the way I was calling it wasnt working... I was calling a histogram on `plt` .. not sure what plt even was.. maybe the module I imported as plt ... ok so it was just a syntax error. need to call a plotting method ON the object to be plotted ... hm a little different from when I used seaborn to plot a heatmap above 

# inspecting unique values to help work out the histogram issue
rooms_uniVals = numColC2['Rooms'].unique()
print(rooms_uniVals) # [ 2  3  4  1  6  5  8  7 10]

#plt.show()

######----- Categorical feature work  -----####################################### 
#print(nonNumericCols.columns)













