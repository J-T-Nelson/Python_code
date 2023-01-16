



# w/o list comprehension
x = [1, 2, 3]
x_squared = []
for x_i in x:
    x_squared.append(x_i**2)
print(x_squared)

# w/ list comprehension
x = [1, 2, 3]
x_squared = [x_i**2 for x_i in x]
print(x_squared)


# set comprehension
x = [1, 2, 3]
x_squared = {x_i**2 for x_i in x}
print(x_squared)


# dict comprehension
x = [1, 2, 3]
x_squared = {x_i: x_i**2 for x_i in x}
print(x_squared)


# multiple funcs in a list comprehension 
def multiply(x, m):
    return x*m
def square(x):
    return x**2
x = [1, 2, 3]
x_squared_list = [multiply(square(x_i), 3) for x_i in x]
print(x_squared)


# filtered comprehension
x = [1, 2, "a", 3, 5]
integers = [x_i for x_i in x if isinstance(x_i, int)]
integers # [1, 2, 3, 5]

# EX 2... NOt sure if this is computationally efficient.. kinda depends on lower level stuff like what the compiler does when it sees this 
x = [1, 2, 3, 4, 5, 6]
x_squared = [x_i**2 for x_i in x if x_i**2 % 2 == 0]

# more efficient version of above example using the 'walrus operator'. 
x = [1, 2, 3, 4, 5, 6]
x_squared = [y for x_i in x if (y := x_i**2) % 2 == 0]

# Further conditional filtering: 
x = [1, 2, "a", 3, 5]
res = [x_i**2 if isinstance(x_i, int) else x_i for x_i in x]
print(res) #[1, 4, 'a', 9, 25]

# more conditional filtering... the ordering of assignment for the walrus operator is a bit confusing here
x = [1, 2, 70, 3, 5]
res = [y if (y := x_i**2) < 10 else 10 for x_i in x]
res #[1, 4, 10, 9, 10]

# some enumeration combined with list comprehension... 
texts = ["whateveR! ", "\n\tZulugula RULES!\n", ]
d = {i: txt for i, txt in enumerate(texts)}
d





# ENUMERATE(): I do understand the idea of this function.. but actually using it.. syntactically and logically is difficult because I don't quite get its limitations. 

testerr = ['af','af','af','af','af','af','af','af','af']
ts = enumerate(testerr)
print(type(ts)) # <class 'enumerate'>
print(ts) # <enumerate object at 0x00000171A4D77B00>

tss = {i:test for i, test in enumerate(testerr)}
print(tss) # {0: 'af', 1: 'af', 2: 'af', 3: 'af', 4: 'af', 5: 'af', 6: 'af', 7: 'af', 8: 'af'}


for indx, t in enumerate(testerr):
    print(indx, t)

# set comprehension test: 

sset = {i for i in testerr}
print(sset) # totally works! 

# MAP() 


org_list = [1, 2, 3, 4, 5]

# define a function that returns the cube of `num`
def cube(num):
    return num**3
   
fin_list = list(map(cube, org_list))
print(fin_list) # [1, 8, 27, 64, 125]


# w/ lambda func: 
fin_list = list(map(lambda x:x**3, org_list))
print(fin_list) # [1, 8, 27, 64, 125]


# ex #2
org_list = ["Hello", "world", "freecodecamp"]
fin_list = list(map(len, org_list))
print(fin_list) # [5, 5, 12]


# EX with multiple lists taken in to accomodate multiple args in pow() 
base = [1, 2, 3, 4]
power = [1, 2, 3, 4]

result = list(map(pow, base, power))
print(result) # [1, 4, 27, 256]



# not really sure when I would want to use map() vs a listComp at this point, but it is good to be able to read them now!


# Generator expression: not sure what they do.. 

x = [1, 2, 3]
x_squared = (x_i**2 for x_i in x) # parens in the syntax of a list comprehension.. 
x_squared # <generator object <genexpr> at 0x00000171A4D2C820>