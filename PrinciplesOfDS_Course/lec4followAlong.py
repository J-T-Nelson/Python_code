import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

houses = pd.read_csv("../Python_code/PrinciplesOfDS_Course/KaggleWork/KaggleData/melb_data.csv")

######----- Data exploration / understanding review -----####################################### 

print(houses.info()) # THIS IS HOW YOU UNDERSTAND YOUR DATA MOST EFFICIENTLY 
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 13580 entries, 0 to 13579
# Data columns (total 21 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   Suburb         13580 non-null  object
#  1   Address        13580 non-null  object
#  2   Rooms          13580 non-null  int64
#  3   Type           13580 non-null  object
#  4   Price          13580 non-null  float64
#  5   Method         13580 non-null  object
#  6   SellerG        13580 non-null  object
#  7   Date           13580 non-null  object
#  8   Distance       13580 non-null  float64
#  9   Postcode       13580 non-null  float64
#  10  Bedroom2       13580 non-null  float64
#  11  Bathroom       13580 non-null  float64
#  12  Car            13518 non-null  float64
#  13  Landsize       13580 non-null  float64
#  14  BuildingArea   7130 non-null   float64
#  15  YearBuilt      8205 non-null   float64
#  16  CouncilArea    12211 non-null  object
#  17  Lattitude      13580 non-null  float64
#  18  Longtitude     13580 non-null  float64
#  19  Regionname     13580 non-null  object
#  20  Propertycount  13580 non-null  float64
# dtypes: float64(12), int64(1), object(8)
# memory usage: 2.2+ MB
print(houses.describe()) # sumamry statistics 

# line plot to see extreme values 
plt.plot(houses['Rooms'])
plt.plot(houses['Landsize'])
plt.show() # think I am only seeing landsize like this.. not getting multiple plots output... YES this is true 

houses.hist(bins=50, figsize=(20,15))
plt.show()

plt.boxplot(houses['Landsize'], vert=False) # there is an extreme outlier making this difficult to see at all
plt.show()
# for plotting multiple things to inspect data, I can see why notebooks can be useful.. as one can easily separate which plots they want to see, instead of having to comment out previous plots. Maybe Jyupiter notebooks is useful for data exploration in this sense... I am sure there are workarounds in this script environment as well though 
# ONE WORKAROUND. using shift+enter allows for one to create an interactive environment where individual plots can be rendered. Still, a bit less clean than working in a notebook environment 

corrs = houses.corr()
# corrs.style.background_gradient() # still not getting a useful output from this.. not sure why 

cgHouses = houses.select_dtypes('object')
print(cgHouses)
print(cgHouses.info())
cgInfo = cgHouses.info() # I think this is just text readout.. maybe we can make a data frame of it though 
cgInfo2 = cgHouses.info
print(type(cgInfo), type(cgInfo2)) # <class 'NoneType'> <class 'method'>

cgInfoDF = pd.DataFrame(cgHouses.info())
print(type(cgInfoDF)) # <class 'pandas.core.frame.DataFrame'>
print(cgInfoDF) #Empty DataFrame
                #Columns: []
                #Index: []
# ^^ so above we just made an empty data frame.. because the type of cgHouses.info() is none.. its just text output.. and I guess the DataFrame method cannot handle that.. it may not even register as text at all as it may just be directly creating output for sys.out without creating intermediate data. (not totally sure if what I am saying makes sense )

######----- Visualizing some categoricals -----####################################### 

houses['Type'].value_counts().plot(kind='bar') # little histogram was pooed out 
plt.show()

houses['Type'].value_counts().plot(kind='pie')  #pie
plt.show()



######----- Notes from pandas video: 25 Nooby Pandas Coding Mistakes.. -----####################################### 

# use df.query('Year > 1925') to make simple or complex queries against a data frame for subsetting.. efficient and concise 
#  Further: '@' can be used to reference variables within the string argument to the query to pull them from the environment being programmed in 
#    further: df.query('Year < 1980 and Time > 10') <- this is how you do and statements.... there may be some sytax to learn for the query method, but it seems worth while

# When writing a CSV .. don't include the indices... `df.to_csv('outputfile.csv', index=False)` <- this removes the index col from the export.. preserving its natural structure 

# don't fillna() with `inplace` option... instead do explicit overwriting: `df = df.fillna(0)`

# Vectorization over for loops: 
#   `df['result'] = df['Year'] > 1900` <- assigning a new column (boolean col) to our DF by digesting a column within the dataFrame 
#  ex2: df['year_squared'] = df['Year']**2 <- this is cleaner and faster than using df.apply(lambda:..... ....)

# DON'T modify the original when you intend to modify a copy
#    df_fast = df.query('Time < 10').copy() <- this makes a new data structure in memory instead of modifying a slice of the old DF
#    df_fast = df.query('Time < 10') <- this modifies a slice of the original dataFrame. Which is really cool, but will not create a new, separate structure in memory 

# chain commands when possible for .. many reasons.. just don't use more variables than necessary insofar as the code is still readable 




































