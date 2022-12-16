# ARTICLE LINK: https://towardsdatascience.com/benchmarking-python-code-with-timeit-80827e131e48

# the different APIs of this basic benchmarking module offer the ability to test snippets of code versus functions, when you want to do each depends on the context in which you're testing. If youre interested in know the base efficiency of two problem solutions for example, they would need to be called in the same way in order to have the same overhead, however, if you simply wanted to test the efficiency of the code at a base level without functions wrapping the code you would instead use the snippet based calling method. 

# I do wonder how the snippet based calling works when you're calling a really large amount of code though, as it seems strange to have code-formatted multiline strings. I will have to test this. 

# another point of curiosity: When does it make sense to functionalize my code versus not functionalizing it? Truthfully, a single python script can be called from the commnad line with arguments provided, thus if I know how to properly script in python I would be able to reduce function definitions and make code more sleek and efficient by not wrapping everything in the code itself, but instead maintaining code based solutions as individual scripts. 

# the reason why its useful to take the min() of your benchmarks instead of mean is because we are interested in understanding the code's speed, not the system's variance. By taking mean, we more strongly account for system (OS) variance, and are tailoring the benchmark to our specific machine, but generally speaking code is to be distributed and used by other machines as well, thus the use in measuring as close to the codes 'real' run time, as it will be more meaningful if every measurement is compared in this way for understanding performance in a context in-specific way.

import timeit

def make_list():
    return [_ for _ in range(10)]

t3 = timeit.repeat(make_list) # also callable API

setup = "def make_list(): return [_ for _ in range(10)]"

t1 = timeit.repeat("make_list()", setup=setup) # callable API
t2 = timeit.repeat("[_ for _ in range(10)]") # snippet based API
print(t1)
print(t2)
print(t3)


def bestTime(t, digits = 4):
    return (round(min(t), digits))

print("Best t1: " + str(bestTime(t1)))
print("Best t2: " + str(bestTime(t2)))
print("Best t3: " + str(bestTime(t3)))



literal = timeit.repeat("{}") # this is called the 'literal' expression for a dictionary 
func = timeit.repeat("dict()") # this is the functional expression for creating a dictionary 

def make_dict():
    return({})

#myFunc = timeit.repeat("make_dict()") # there is some error being thrown : NameError: name 'make_dict' is not defined ... not sure what is happening here.. the article writer suggested I test this. 

print("best literal: " + str(bestTime(literal)))
print("best func: " + str(bestTime(func)))
#print("best myFunc: " + str(bestTime(myFunc)))


# notice the tripple quotes below which allow for multiline quotes! 

setup = """import array
def foo_array(n):
    return array.array("i", [0]*n)
def foo_list(n):
    return [0]*n
"""
number = 100
rep = 5
t4 = timeit.repeat("foo_array(10_000_000)", setup=setup, number=number, repeat=rep)
t5 = timeit.repeat("foo_list(10_000_000)", setup=setup, number=number, repeat=rep)

print(t4)
print(t5) # this code block seems to take a long time, or seems to not work generally. .. it just take a long time 
#print('printing to ensure things work')