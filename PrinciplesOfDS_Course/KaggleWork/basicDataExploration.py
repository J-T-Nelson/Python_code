import pandas as pd

# Progress with Kaggle was a little bit slow.. I think I was mostly learning their tutorial format so far.. where to locate things... etc. I will continue with the basics of machine learning next sessions and hopefully move a long a little more smoothly. The content does seem useful for class. 


melb_fileP = "D:\\Programming\\Python_code\\PrinciplesOfDS_Course\\KaggleWork\\KaggleData\\melb_data.csv"

melbData = pd.read_csv(melb_fileP)

print(melbData.describe()) # nothing printed... need print method in a script 
print(type(melbData)) # <class 'pandas.core.frame.DataFrame'>

#The first number, the count, shows how many rows have non-missing values.
# To interpret the min, 25%, 50%, 75% and max values, imagine sorting each column from lowest to highest value. The first (smallest) value is the min. If you go a quarter way through the list, you'll find a number that is bigger than 25% of the values and smaller than 75% of the values. That is the 25% value (pronounced "25th percentile"). The 50th and 75th percentiles are defined analogously, and the max is the largest number.

######----- Your First Machine Learning Model 3/7 -----####################################### 

print(melbData.columns)

# dropna drops missing values (think of na as "not available")
melbData = melbData.dropna(axis=0) # 0 refers to rows... as its the first dim of the DF. so we are dropping all rows with missing values 

#You can pull out a variable with dot-notation. This single column is stored in a Series, which is broadly like a DataFrame with only a single column of data.
# We'll use the dot notation to select the column we want to predict, which is called the prediction target. By convention, the prediction target is called y. So the code we need to save the house prices in the Melbourne data is
y = melbData.Price

# features are the cols/variables used to make preditions about our prediction target 
# selecting features: 
melbFeatures = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude', 'BuildingArea', 'YearBuilt']
# by convention, feature data is saved as 'x' 

X = melbData[melbFeatures] # subsetting the DF by col name... simplified syntax... (I think if I used indices with the same syntax I would be grabbing rows.. )
rowGrab = melbData[1:5]
print("\nPrinting rows 1:5", "\n", rowGrab)
print(rowGrab.describe()) # count = 4.. so yeah same indexing as string slicing for python
print(X.describe())
print(X.head()) # we can see that some rows are removed.. like 3 and 5, must have had 'na' vals somewhere 

# Visually checking your data with these commands is an important part of a data scientist's job. You'll frequently find surprises in the dataset that deserve further inspection.

# Scikit-learn is easily the most popular library for modeling the types of data typically stored in DataFrames.

# The steps to building and using a model are:

# Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
# Fit: Capture patterns from provided data. This is the heart of modeling.
# Predict: Just what it sounds like
# Evaluate: Determine how accurate the model's predictions are.

from sklearn.tree import DecisionTreeRegressor # `pip3 install -U scikit-learn`  <- this command worked for successful install.. not sure what pip3 vs pip is.. not sure what -U flag means either 
# The command pip install -U scikit-learn scipy matplotlib installs or updates the packages scikit-learn, scipy, and matplotlib to the latest version available on the Python Package Index (PyPI).

# pip and pip3 are both package managers for Python, but they are used to manage different versions of Python.

# pip is the default package manager for Python 2, and it is used to install and manage packages for Python 2.x versions. It is usually included with Python 2.7.9 and later versions.

# pip3 is the package manager for Python 3, and it is used to install and manage packages for Python 3.x versions. It is usually included with Python 3.4 and later versions.

# The main difference between pip and pip3 is that pip installs packages for Python 2, while pip3 installs packages for Python 3. This is important because some packages are not compatible with both versions of Python and may not work correctly if installed with the wrong package manager.

# Define model. Specify a number for random_state to ensure same results each run
melbModel_1 = DecisionTreeRegressor(random_state=1)
# Fit model
melbModel_1.fit(X, y)


#Many machine learning models allow some randomness in model training. Specifying a number for random_state ensures you get the same results in each run. This is considered a good practice. You use any number, and model quality won't depend meaningfully on exactly what value you choose.

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbModel_1.predict(X.head()))

######----- Model Validation -----####################################### 

#the relevant measure of model quality is predictive accuracy. In other words, will the model's predictions be close to what actually happens.

#Many people make a huge mistake when measuring predictive accuracy. They make predictions with their training data and compare those predictions to the target values in the training data. 

#You'd first need to summarize the model quality into an understandable way. If you compare predicted and actual home values for 10,000 houses, you'll likely find mix of good and bad predictions. Looking through a list of 10,000 predicted and actual values would be pointless. We need to summarize this into a single metric.

# Mean Absolute Error (Mean absolute error)

# The prediction error for each house is:  error=actual−predicted
# So, if a house cost $150,000 and you predicted it would cost $100,000 the error is $50,000.
# MAE will give us our on average error

from sklearn.metrics import mean_absolute_error

predictedMelbPrices = melbModel_1.predict(X)
melbMAE = mean_absolute_error(y, predictedMelbPrices)
print("melbMAE:", melbMAE) # melbMAE: 434.71594577146544

# The measure we just computed can be called an "in-sample" score. We used a single "sample" of houses for both building the model and evaluating it. Here's why this is bad.
# confounding variables is why this is bad 

# Since models' practical value come from making predictions on new data, we measure performance on data that wasn't used to build the model. The most straightforward way to do this is to exclude some data from the model-building process, and then use those to test the model's accuracy on data it hasn't seen before. This data is called validation data.

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbModel_1 = DecisionTreeRegressor(random_state=0)
melbModel_1.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbModel_1.predict(val_X)
print("MAE of train test split operation:", mean_absolute_error(val_y, val_predictions)) # 261323.02905100066


######----- Underfitting and OVerfitting -----####################################### 






















































