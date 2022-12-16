

from collections import Counter
import time


s = ' A sentence with whitespace. \n'

print('{}'.format(s.lstrip()))
print('{}'.format(s.rstrip()))
print('{}'.format(s.strip())) # not sure what the curly braket .format() is doing in this case... output is no different from totally excluding it. 
print(s.strip())
print(s.strip('e'))
print('{}'.format(s.strip('e'))) # so no 'e' is being removed from either command, this is because it is only checking the outside of each string I think

s2 = 'eeeee' + s + 'eeee'
print(s2)
print('{}'.format(s2.strip('e'))) 
print(s2.strip('e')) # now the e's are being stripped as they are occuring at the start and end... well the new e's I added to s2 

def function_a(x):
  print('sleeping {}'.format(x))
  time.sleep(x)
  return

print(time.gmtime(0))

# function_a(2)




# def gen_point():
#     return 'POINT ({})'.format(
#         gen_coords(),
#     )

s1 = 'perpendicular'
s22 = 'pen'
s3 = 'pep'
print('\'pen\' in \'perpendicular\': {}'.format(s22 in s1))

print('\'pep\' in \'perpendicular\': {}'.format(s3 in s1))

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram(s1,s2), "this is s1, then s2: " + s1 + " ::: " + s2)


# 2022 12 11


# testing the 'with' keyword
with open("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\GCcontTest.txt", 'r') as fileIn2:
    for line in fileIn2:
        print(line, end="")

#vs no 'with' keyword

fileIn3 = open("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\GCcontTest.txt", 'r')
for line in fileIn3:
    print(line, end="")

# both work just fine... so I guess I need to take another look at the above code to see why I had issues. 


# testing on 12-14-2022

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass
i = 1
for cls in [B, C, D]:
    print(i)
    i+=1

    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")




fileIn = open("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\GCcontTest.txt", 'r')
lineOne = fileIn.readline() # seems readline naturally truncates '\n' ... while .next() in an iterator setting does not. 
print(lineOne)
print(len(lineOne))
print(fileIn.tell())

lineTwo = fileIn.readline()
print(lineTwo)
print(len(lineTwo))
print(fileIn.tell())

lineThree = fileIn.readline()
print(lineThree)
print(len(lineThree))
print(fileIn.tell())

fileIn.seek(16)
lineOne2 = fileIn.readline()
print(lineOne2) # IMPORTANT NOTE: the .tell position is always an integer which is = the the previous lines len()+1. so if line 1 has 15 chars, then after a single .readline(), .tell() will be at 16. For each readline, another +1 is added to the sum total of chars ... I don't if this has or hasn't accounted for '\n' at this point... doesn len count \n? ... SEE EXAMPLE BELOW. yes it is counting the '\n', and its those characters responsible for adding 1 to each line's tell positon. 

tStrang1 = 'thisisatest'
tStrang2 = 'thisisatest\n'
print("len 1: " + str(len(tStrang1)) + "  len 2: " + str(len(tStrang2))) # len 1: 11  len 2: 12

fileIn2 = open("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\GCcontTest.txt", 'r')
fileCont = fileIn2.readlines() # this generates a list / array of strings. 
#contArray = fileCont.split(">")
print(fileCont)
# ^^ I wanted to see if somehow splitting up the content of the file would be a useful way to put entries into a dictionary / determine our solution.. no dice though. 


x = 10_000_000
print(x)

