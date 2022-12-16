# using this doc to study other peoples answers, as I had a pretty hard time working through the example and I believe other peoples approaches will be interesting to study. Want to study 2-3 at most, as more than that will certainly be too much. 


testFile = "D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\GCcontTest.txt"

s1 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

countG = s1.count('G')
countC = s1.count('C')
countGC = countG + countC
finalpercent = 100* (countGC/len(s1))
print(finalpercent) # checks out and works well. ... didn't know I could use .count. 

# serolos2 solution: 

#count GC contents percentage
def count_GC(x): 
    p = 0
    p += x.count('G')
    p += x.count('C')
    GC_percentage = (p/(len(x)))*100
    return GC_percentage

library = open('D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc (1).txt', 'r')
keys = []
strands = []
fragment = ''

#create lists with given strands and keys to them
for line in library:
    if line[0] != '>':
        fragment += line
        fragment = fragment.rstrip() #remove all blank symbols from a string, otherwise you get wrong answers
    elif line[0] == '>':
        keys.append(line[1:14]) # doing 14 instead of nothing here means no \n character is at the end of the key which saves steps later on. 
        strands.append(fragment)
        fragment = ''

#add last strand to the list and remove unneccessary '' from it
strands.append(fragment)
strands.remove('')

#create a dictionary, storing keys and GC percentages 
percentages = {}
for y in range(len(keys)):
    percentages[keys[y]] = count_GC(strands[y])

#find max GC contents and according key, print
max_key = max(percentages, key=percentages.get)
print(max_key, '\n', round(percentages[max_key], 6))

library.close()


# tomorrow I want to benchmark my solution against serolos2 as well as 1 other solution which I read about. Serolos2 had much more elegance in his problem soliving at some points like his inverse for loop in particular which would have really cleaned up my own code. However, I am not sure why he takes the time to remove empty space.. maybe something I did automatically took care of that for me. I do like the clear delination of one task to the next in his solution however, as each block of code for the most part clearly addresses one single problem. I don't really get how he is using the max function here... also good to see the round() function! 

# ok so tomorrow, look into benchmarking enough to begin benchmarking your work versus other peoples work. Figure out how to make all that happen. 