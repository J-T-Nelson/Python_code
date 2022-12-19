# HOW map() WORKS:

#In Python, the map() function is a built-in function that applies a specified function to each element of an iterable (such as a list, tuple, or string). The map() function returns a new iterable with the modified elements.

# define a function that takes a number and returns its square
def square(x):
  return x * x

# create a list of numbers
numbers = [1, 2, 3, 4, 5]

# use the map function to apply the square function to each element of the list
squares = map(square, numbers)

# print the resulting list
print(list(squares))  # Output: [1, 4, 9, 16, 25]



#You can also use the map() function with multiple iterables. In this case, the function should take as many arguments as there are iterables. The map() function will apply the function to the corresponding elements of each iterable.

# define a function that takes two numbers and returns their sum
def add(x, y):
  return x + y

# create two lists of numbers
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# use the map function to apply the add function to the corresponding elements of each list
sums = map(add, list1, list2)

# print the resulting list
print(list(sums))  # Output: [5, 7, 9]


#Keep in mind that the map() function returns a map object that is an iterator. To see the modified elements, you need to convert the map object to a list or another iterable.



print(type(sums)) # Output: <class 'map'>



