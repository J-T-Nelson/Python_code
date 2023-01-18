import math
import numpy
print("MATH MUTHAFUCKA, {}".format(type(math)))

# math is a module. A module is just a collection of variables (a namespace, if you like) defined by someone else. We can see all the names in math using the built-in function dir().
print(dir(math))

print(math.pi, "num digits:", len("141592653589793")) # 15 digits 
print(math.e)

print(math.log(32, 2))

# TO GET HELP WITH A FUNCTION: 
print(help(math.log))

# TO IMPORT ALL THINGS WITHIN A MODULE S.T. the variable names can be used without referencing the module itself... careful here though as you are generating more taken variable names which means you limit the names available in hidden ways ... this also opens up the possibility of masking the namespace of a given module if they have functions / variables of the same name as well! ('shadows' is synonymous with 'masks')

# from math import *
# print(pi, log(32, 2))

# modules also can have submodules: 
print("numpy.random is a submodule.. see its type:", type(numpy.random)) # numpy.random is a submodule.. see its type: <class 'module'>

rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls) # [5 1 2 2 2 5 5 4 3 5]

# Operator Overloading: 
# this is basically the idea of non-standard evaluation in R, where core operators can be defined to have different (even clashing) behvaiors wrt base operators. So similar to R, (I think) numpy allows one to add 10 (+ 10) to a whole array with simple syntax. `array1 +10` for example 



xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x)) # numpy has implicit behavior which differs where arrays of arrays are automatically interpreted as matrices it appears 
# xlist = [[1, 2, 3], [2, 4, 6]]
# x =
# [[1 2 3]
#  [2 4 6]]

# Get the last element of the second row of our numpy array .......... Indexing also R-like
print(x[1,-1]) # 6
print(type(x)) #<class 'numpy.ndarray'>

# Tensorflow uses extensive amounts of operator overloading 

#pandas DataFrame example
# Get the rows with population over 1m in South America
#df[(df['population'] > 10**6) & (df['continent'] == 'South America')]


# # ON DOUBLE UNDERSCORES: (they are for operator overloading??)
# When Python programmers want to define how operators behave on their types, they do so by implementing methods with special names beginning and ending with 2 underscores such as __lt__, __setattr__, or __contains__. Generally, names that follow this double-underscore format have a special meaning to Python.

#So, for example, the expression x in [1, 2, 3] is actually calling the list method __contains__ behind-the-scenes. It's equivalent to (the much uglier) [1, 2, 3].__contains__(x).
# ^^^^^^^^ THIS EXAMPLE READS LIKE A TYPE OF ALIAS TO ME 

# CHAT_GPT ON DUB UNDERSCORES: 
# Variables in Python that are surrounded by double underscores, such as __abs__ and __add__, are special variables called "dunder methods" or "magic methods". Dunder stands for "double underscore". These methods are used to define the behavior of certain operations in Python classes.

#When a class defines a dunder method, it tells Python how to handle a specific operation when it is performed on an instance of that class. For example, __add__ method tells Python how to handle the "+" operator when it is used on an instance of that class. __abs__ method tells Python how to handle the "abs()" function when it is used on an instance of that class.

#You can think of dunder methods as special methods that give classes the ability to define their own behavior for common operations. These methods are used to define the behavior of classes and objects in Python, so they are important for creating custom classes and objects.

#On the other hand, variables without underscores, called "regular variables", are used to store data in classes and objects. These variables are used to define the state of a class or object.


