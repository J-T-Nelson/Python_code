
def Hypotenuse(a, b) : 
    sq1 = a*a;
    sq2 = b*b;
    c_squared = sq1+sq2;
    return(c_squared)


print(Hypotenuse(3,4))
print(Hypotenuse(3,5))
print(Hypotenuse(868, 802))

# is this a comment in python? I think so! 
list1 = ["dog", "cat", 'ham', 'mam']
list2 = ['floor', 'flogging', 'fugging', 'shrugging']
list3 = ['sleep', 'seep', 'creepy', 'meep']
list4 = [list1, list2, list3]

# print("This is list4: " + list4[1])  # <- type error here

print("This is list3[1]: " + list3[1])
print("This is list4[1][2]: " + list4[1][2]) # sweet the referencing that I am used to from R is also used here! 

# print("default print method for list1: " + list1) # cannot concatenate it with a string.. but can print it alone... hmm 

# print("default print method for list1: " + list1.__str__) # <- still not working for concatenation ... no idea what the str thing is doing actually. 

# listString =  # was tryiing to find casting or some to string method.. but no dice.  

# list3[4] = 'Ill fok yur mum' <- ERROR: "list assignment index out of range" 
list3.append("ill fok yur mum")
print(list3)
list3[2] = "i'll beat your head with your own head dude." # <- this does work for reassignment, but does not automatically call an append function if you're to attempt to assign values to list positions which currently don't exist
print("Demonstrating my skills with lists and printing n shit: ", end="")
print(list3)

print("gonna check out grabbing with the good notation.. : ")
print(list3[2:4]) # damn that is cool. 

bigString = "ImadeThisStringSuchThatItCanBeProductivelySlicedIThink"

print(bigString[4:20])

def twoPointStringGrabber(String, a, b, c, d):
    string1 = String[a:b+1]
    string2 = String[c:d+1]
    list1 = [string1, string2]
    print(list1)
    print(string1 + " " + string2)
    return (list1)

twoPointStringGrabber("8Buh7mxt1XU2Drv0Hpeis7Ejh36K05fmIRl5G6g3nXv1MkKGrbgz79Oenanthe3o5Suno8b6iDQNAWQ9uXGeiGalpestris3kPxjU97lYPE0SAbWjRNgJxM0f9WBaTgAWVCEE1zqPgj1bndD3xUb13j3OO7GXTPspvE9y5XPyVHVNPA.", 4, 61, 86, 94)

twoPointStringGrabber("HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.", 22, 27, 97, 102)

twoPointStringGrabber("z60lqKyQHjizDLx3HSQoy5eaAqbp9fsSGk9cOz2e7LepidobatrachushhgudMxvulgarisYiIu77Wv7UpjmUxduIFgx8aiFxFl2CxQTHvgWTgRfF76SdPJ3tOoBPUtwvUtpVkSYAT2dvJhomVVipvzbD183CtQCt64WKxFPymrWo5z0SNLJy.", 41, 55, 63, 70)

n = 10
for i in range (n):
    print(i)
# ^^ prints 0:9 ... notably sticking to the index base 0 form of python. so range(n) = [0:n-1]

print(range(5, 12)) # not sure why but this doesn't print the range.. it prints "range(5, 12)" as if it were a string... weird 
print("range(5, 12)") 

# print(range(5, 12) + 1) # type error here... 

strung = range(5,12)
print(strung) # still not printing it out as a string... but the for loop is working so there is a built in itterator of sorts working underneath here. 
print(str(strung)) # still printing 'range(5,12)' 
strang = str(strung)
print(strang) # STILL PRTING THE SHAME SHIT... hm. 
#print(' '.join(strung)) # error
print(list(strang)) # ['r', 'a', 'n', 'g', 'e', '(', '5', ',', ' ', '1', '2', ')'] ... WEIRD. The text of the code itself is being turned into a string.. like no interpretation of the code at all. That is remarkably strange. 
strr = list(range(5, 20))
print(strr) # This is what I was looking for. !!! so range(x,y) is not itself a list... but seems to be ... idk. an upper and lower bound? I wonder how functions like the for() loop interpret 'range()' 
for i in strung:
    print(i)

st = "DogWater"
len(st)
for i in st:
    print(i)
for i in range(len(st)):
    print(i, st[i])

# FOLLOWING ALONG WITH A STANFORD WEBPAGE FOR MORE LEARNING: 
for i in reversed(range(10)): # we are printing 9 8 7 6 ... 0
    print(i) 

r1 = list(range(20))
r2 = list(range(10, 2540, 56))
r3 = r1 + r2 # composing lists with the addition symbol 
print(r1)
print(r2)
print(r3)

cities = ['Madrid', 'Barcelona', 'Valencia', 'Munich', 'Stuttgart'] # gonna look at the different ways of subsetting lists... 
cities[:3] #['Madrid', 'Barcelona', 'Valencia'] ... This is exclusive.. as its really indeces 0-2 (0, 1, 2)
cities # ['Madrid', 'Barcelona', 'Valencia', 'Munich', 'Stuttgart'] ... not a subset.. just gets the whole list
cities[::3] # ['Madrid', 'Munich'] ... seems to grab just 0 and 3 ... interesting. 
cities[0::3] # ['Madrid', 'Munich']
cities[0::1] #['Madrid', 'Barcelona', 'Valencia', 'Munich', 'Stuttgart'] ... OK this :: means access stepwise from a starting point then? 
cities[0::2] #['Madrid', 'Valencia', 'Stuttgart']
cities[1::2] # ['Barcelona', 'Munich'] EXACTLY .. its stepwise access with the size of the steps being specified and the starting point being specified. 
cities[2:] # very strange.. but noted.. this accesses elements STARTING from 2 and ending at the end. maybe not strange.. makes sense. 
cities[:-2] # ['Madrid', 'Barcelona', 'Valencia'] ... no negative access like this.. (there is probably a way to achieve what I was attempting though)
cities[-1] # 'Stuttgart' .. negative access of single values works well though

cities[:2] = ['newcity', 'fokEurp']
cities # ['newcity', 'fokEurp', 'Valencia', 'Munich', 'Stuttgart'] ... multiple entries of an array can be rewritten at once
cities = ['no diggy'] 
cities # ['no diggy'] ... the whole object can easily be overwritten as well.. which is obvious. 

numeralSet = {1, 2, 3, 4, 6, 4}
numeralSet[2] #File "<stdin>", line 1, in <module>  TypeError: 'set' object is not subscriptable .... cannot access set elements by positions as sets are fundamentally unordered 


products = ['table', 'chair', 'lamp', 'closet', 'bed', 'shelf', 'computer']
del products[1:4] # del keyword seems to allow for deletion of items within a collection.. not sure which collections its able to access. 
products #['table', 'bed', 'shelf', 'computer'] ... again its inclusive for the starting index and exclusive for the ending index.. 
# del products
# products #File "<stdin>", line 1, in <module>  NameError: name 'products' is not defined ... del keyword can also be used to just remove whole objects
print(products.pop(2)) # shelf ... pop method returns and removes an object at the specified index. 
products.remove('table')
products # ['bed', 'computer'] ... .remove removes something without returning it.. useful, as something can be removed by name. 
products.remove('dogCat') # File "<stdin>", line 1, in <module>   ValueError: list.remove(x): x not in list

products.insert(0, 'HAM')
products # ['HAM', 'bed', 'computer'] ... insertion by index 
products.insert(len(products), 'dogfist')
products  #  ['HAM', 'bed', 'computer', 'dogfist'] ... using len() to insert at the very end of a list 
products.append('lastITEM')
products # ['HAM', 'bed', 'computer', 'dogfist', 'lastITEM'] ... .append() is a more direct way of adding to the end of a list 
products.insert(-2,'bedMan')
products # ['HAM', 'bed', 'bedMan', 'computer', 'dogfist'] ..  negative index insertion..

print(sorted(products)) # ['HAM', 'bed', 'computer', 'dogfist', 'lastITEM'] ... no change.. 'sorted()' however, is supposed to return a sorted list, but doesn't modify the original input list itself.. so it returns a sorted copy.  

sortedProducts = sorted(products)
sortedProducts # ['HAM', 'bed', 'bedMan', 'computer', 'dogfist', 'lastITEM'] ... no alphabetic sorting still.. hmm 
products # ['HAM', 'bed', 'computer', 'bedMan', 'dogfist', 'lastITEM']
products.sort()
products # ['HAM', 'bed', 'computer', 'bedMan', 'dogfist', 'lastITEM'] ... still no sorting occurring. 

 # to sort by first letter... 
sortedProd = sorted(products, key = lambda x: x[0])
sortedProd # ['HAM', 'bed', 'bedMan', 'computer', 'dogfist', 'lastITEM'] ... ok alphabetic sorting may not be working... idk.. are caps important for such comparison
sortedProd_2 = sorted(products, key = len)
sortedProd_2


letters = ['i', 'c', 'v', 'b', 'a', 'H', 'j', 'A', 'B']
letters
sortLetters = sorted(letters)
sortLetters # ['A', 'B', 'H', 'a', 'b', 'c', 'i', 'j', 'v'] ... ok confirmed. caps are placed in front of lower case... so our products list was literally already sorted alphabetically by first letter AND it was already sorted by length. lol. ok. 

sortedProd_3 = sorted(products, key = lambda x: x[1]) # sorting by 2nd letter ...
sortedProd_3  #['HAM', 'lastITEM', 'bed', 'bedMan', 'computer', 'dogfist'] .. it worked... but the list is also ALMOST exactly in order by second letter as well. wtf. 



g = range(10, 30)
for i in g:
    print(i)

def sumOddInts(a,b):
    span = range(a, b)
    spanSum = 0
    for val in span:
        if(val % 2 == 1):
            spanSum += val

    return(spanSum)

testSS = sumOddInts(100, 200)
print("testing sumOddInts, expecting output to be 7500: " + str(testSS)) # type error... cannot concatenate int to str... (surprising) ... seems str() is the means of converting something to a string. 
# SUCCESS!! 

testSS2 = sumOddInts(4228, 9166)
print(str(testSS2)) 


'''This is a block comment in python I think
I can just keep typing inbetween 3 apostrophes... '''
# Apparently official style guides suggest that you just use multiple lines of hashtaggingin order to do multi line comments though
# like this... what is the hotkey in VS code to make this easier though? 


#testerFile = open('Rosalind_BioInfo_Challenges\\testerFile1.txt', 'r') # reading in the file I just made

# for line in testerFile:
#     print(line.count)

# for line in testerFile:
#     print(line.count())
#           ^^ THIS IS WHAT COUNT DOES: Return the number of non-overlapping occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.

# for line in testerFile:
#     print(line.upper()) # OK ... using parens obviously is actually calling the method. 

    # before I was just seeing "<built-in method upper of str object at 0x000002A290DE4BF0>" .. which I don't really understand what is happening. It is printing meta info about the method and telling me where the object exists in memory.. so not useless.. just not sure what the purpose of this funcitonality is. 

testerFile = open('Rosalind_BioInfo_Challenges\\testerFile1.txt', 'r')
# SPLITTING THE WHOLE FILE BY LINES INTO A LIST: 
fileList1 = str(testerFile).splitlines() # ok, so before str() was added, testerFile wasnt actually a string.. it was instead a 'TextIOWrapper' .. basically a file wraper in reading mode. So how do we convert the file wrapper to a big string then? 
print(fileList1)

fileString = testerFile.readlines()
#fileList2 = fileString.splitlines() # THIS NOT WORKING: ... as readlines() returns a list of strings already... so no need to do the splitlines() duhh 
print("printing the list that was generated from the stringified file: ", end="")
print(fileString) # yeesh this is ugly to print, but I sure am printing it 
print(len(fileString)) # this works! 

print("Stripping new line chars from the array and grabbing 1/4th of it to reduce the visual load")

for li in range(int(len(fileString)/4)):
    print(fileString[li].strip())

    
def evenFileLines(filePath, outputFile):
    file = open(filePath, 'r')
    fileList = file.readlines()
    writeFile = open(outputFile, 'w')

    for lin in range(len(fileList)):
        if( (lin+1)% 2 == 0 ):
            writeFile.write(str(fileList[lin]))

evenFileLines('D:\Programming\Python_code\Rosalind_BioInfo_Challenges\Robin.txt', 'D:/Programming/Python_code/Rosalind_BioInfo_Challenges/RosalindPythonTutorial/RobinOutput.txt')


s1 = "write this to file"
fileWtest = open('write.txt', 'w')
fileWtest.write(s1) # success

s2 = "Second string to write... "
fileWtest2 = open('D:/Programming/Python_code/Rosalind_BioInfo_Challenges/RosalindPythonTutorial/ReWrite.txt', 'w')
# fileWtest2.write(s1) #failed to write anything? .. then it succeeded.. then it didn't overwrite itself when both write commands were active... weird behavior going on here. ... also the system seems to be having a hard time with relative paths for some reason?? 
fileWtest2.write(s2) 

# ok spent enough time here. Kind of getting tired of trouble shooting the weirdness.. gonna hit it fresh later. 

evenFileLines("C:\\Users\\Tanner_N\\Downloads\\rosalind_ini5.txt", 'D:/Programming/Python_code/Rosalind_BioInfo_Challenges/RosalindPythonTutorial/questionAnswer.txt')


# PROMPT #6 Dictionaries: 

# What talk to Jordan about? 
# 1. How are programs organized in python? 
#  - like file structure that is? Would a java like file structure be used in any complex set of python scripts? 
# 2. What do you know of writting python extensions?  
# 3. Is there a variety of data structure options available or is python's DSs built moreso for quick usability and thus aren't to be considered as deeply as java DS? 
# 4. more general but applicable... (maybe show him rosalind..) How often do you use classes? How do I know when I would have been wise to use a class instead of using low level DSs? 
# 5. For Rosalind problems, would you suggest trying to learn and use any libraries? 
#  - further, looking at the problem sets, would you have any suggestions on problem sets which I should prioritize if I want to ensure development of machine learning fundamentals? 
# 6. IDEs ... I know he likes to use pycharm... I guess I wonder if he has used VS code for python and would like to know what sorts of features I would have access to from something like pycharm, as I would prefer to not spend time learning new keybindings again if possible, but also if there is strong enough reason to do python in that environment exclusively I wouldn't complain either. 


# good idea to create a virtual envrionment that corresponds to a specific project... it is essentially just a run time.. a group of linked imported packages which are associated with a specific version python (the python interpreter) ... when in this specific virtual environment you can thus control the configuration of versions, resources etc. 

# So look into virtual envrionments... As they are useful for maintaining consitency project to project. I should read more on java VM and understand how it corresponds to pythons behavior as a programming language... as Jordan says the behavior of the python interpreter(?) is similar / essentially the same.. 

# He has interpreter for python 2 and python 3... 

# Python packages have the ability to build virtual environments... Then you can configure it on a script by script basis.. (useful) .. Some IDEs have support for virtual environment support within that space (thus diff envrionemnts can be spun up on a per project basis) ... (anything Jet Brains makes can do this apparently... ) 
# - Venv <- the virtual envrionment package for python... 

# He does prefer pycharm. Why? Its kind of like RStudio for Python... 

# NumPy is pretty base level importance for applications of python in job settings. Therefore pick it up early and start learning it after a bit of knowlege building for base python


# ROSALIND DICTIONARIES PROBLEM... 

# dictionaries are key:value mapping funcs. 
phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
print(phones['Zoe'])
phones['Billy'] = '3000000000 JUNK'
phones # {'Zoe': '232-43-58', 'Alice': '165-88-56', 'Billy': '3000000000 JUNK'}
phones['zoe'] =  '1-800 you a little baby bitch'
phones # {'Zoe': '232-43-58', 'Alice': '165-88-56', 'Billy': '3000000000 JUNK', 'zoe': '1-800 you a little baby bitch'} ... dictionaries are case sensitive when using strings as keys.. only immutible primitive values such as ints floats, strings etc.. They are also unordered fundamentally, as they are functions more than they are collections in that sense. 
for key in phones:
    print(key, phones[key])


'jorn' in phones # False
'Zoe' in phones # True 
# ^^ checking for presence of keys in a dict 
def weGotTheNumber(keyName):            
    if keyName in phones:
        print('we got that number')
    else:
        print('no number like that here sir')

weGotTheNumber('jan') # no number like that here sir ... 
weGotTheNumber('Billy') # we got that number ... 

# ok we need to print out key value pairs and increment the values of a key when that key is found in a sample of text.. 
# so... check if str is a key with 'blank' in dict ... if yes. increment its value if no .. add it to dict 

def countWordsWithDict(string):
    wordCounter = {}
    splitString = string.split()
    for word in splitString:
        if word in wordCounter:
            wordCounter[word] = wordCounter[word] + 1
        else:
            wordCounter[word] = 1
    
    #writing resulting dictionary to a file... 
    fileOut = open('Rosalind_BioInfo_Challenges\\RosalindPythonTutorial\\dictionaryOut.txt', 'w')
    for key in wordCounter:
        fileOut.write(key + ' ' + str(wordCounter[key]) + '\n')

    
    
# how to split strings by a specified character 
s = "We tried list and we tried dicts also we tried Zen"
sSplit = s.split()
sSplit # ['We', 'tried', 'list', 'and', 'we', 'tried', 'dicts', 'also', 'we', 'tried', 'Zen']

# Testing countWOrdsWithDict

countWordsWithDict(s)

dataTest = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
countWordsWithDict(dataTest)
# SUCCESS!! .. sweet. we now know a little more about dictionaries in python... and are ready to move onto actual problems in Rosalind. 






def getSubstrings(string, substringSize = 1):
    
    numSubs = len(string) - len(substringSize) + 1
    ssList = [0]*numSubs

    for i in range(numSubs):
        ssList[i] = string[i: (substringSize+i)]

    print(ssList)
    return(ssList)


def natNumSum(num = 10):
    Sum = (num*(num+1))/2
    return int(Sum)

natNumSum(3)
natNumSum(10)
natNumSum(100)
natNumSum(1000)