# We are seeking for largest common substrings... This seems very open ended to start. 
# obviously substrings will only involve ACGT, however, all possible permutations of 1k ACGT are the set of substrings we are seeking. 
# Most challenging is the fact we don't actually know the substring we want to find, which means we have to just test for... everything...? as efficiently as possible. 
# really not sure where to start here.... 

# I think we must perform a comprehensive search... Obviously this will not be efficent in my implementation, but maybe I can at least be conceptually accurate in my apprach if I cannot be computationally efficient in it as well. 

# for a comprehensive search I need to first identify the smallest string of the set, as that will be the maximum common substring size. (if all are the same then we just start with the first item in the set)
# then I need to check if that smallest string of the set is found in all others (i.e., if that doesn't appear in all others.)
#   finally, checking each possible substring of size x-1, then x-2, then x-3... until x-n = 1 OR until a substring of a given size matches every other substring in the set will provide us the largest common substring. 

# Sample Output == AC

import re

def getSubstrings(string, substringSize = 1):
    numSubs = len(string) - substringSize + 1
    ssList = [0]*numSubs
    for i in range(numSubs):
        ssList[i] = string[i: (substringSize+i)]

    return(ssList)

getSubstrings("Strang", 3) # great! 


def largestCommonMotif(filePath, variableStrLength = False, slicePoint = 13):
    f = open(filePath, 'r')
    fCont = f.read().split(">")[1:]
    f.close()

    DNAseqs = [st[slicePoint:].replace("\n", '') for st in fCont]

    if (variableStrLength): 
        # I could not get the index of the smallest element and instead just remove it by list.remove(item) and the append it to the start with list.insert(0, item)
        sm_string = min(DNAseqs, key=len)
        smallestIndex = DNAseqs.index(sm_string)
        #print(sm_string, "length of this string:", len(sm_string), "\nsmallest Index:", smallestIndex)

        DNAseqs[smallestIndex] = DNAseqs[0]
        DNAseqs[0] = sm_string # now the smallest string is at the front of the list. 
        # print("second time:", DNAseqs) # excellent
    else:
        sm_string = DNAseqs[0] # need a string to reference for size during search for largest motif

        # make list of substrings of size subSize from sm_string, 
        # for each substring in list check if there are matches across all strings within DNAseqs[1:], 
        # if yes, then set fMatch = True, set LCM = successfulSubstring, return LCM
    fMatch = False
    subSize = len(sm_string)
    lcm = ''
    while not fMatch:
        if subSize < 2:
            print("Subsize less than 2")
            break

        subStrings = getSubstrings(sm_string, subSize)
        curSearchResult = False
        for substr in subStrings:
            if curSearchResult: # this is only true when the last seq checked contained a match for the substring, This will not occur with any non-matches occurring
                fMatch = True
                break
            for seq in DNAseqs[1:]: # not sure if I can iterate across a subset like this.. but I sure hope so. 
                if re.search(substr, seq):
                    curSearchResult = True
                    continue
                else:
                    curSearchResult = False
                    break
            if curSearchResult:
                lcm = substr
        subSize = subSize - 1
    print(lcm)
    return lcm
        
# I have very low faith in the quality of my code as its just complicated :( ... my code totally worked.. but other people are getting solutions that are many times more efficient apparently and infact using entirely different data structures as well... Time to study. 

#largestCommonMotif("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\findingAsharedMotif\\sampleData.txt", variableStrLength=True, slicePoint=10) # worked for the test data set... which is so meanially small its just sad... 

# largestCommonMotif("C:\\Users\\Tanner_N\\Downloads\\rosalind_lcsm.txt", variableStrLength=True) # We did eventually get an answer, it just took a very long time. 
largestCommonMotif("C:\\Users\\Tanner_N\\Downloads\\rosalind_lcsm (1).txt", variableStrLength=True)
# CTAATACCCCAGTATCAACTGTCTCATGACACATGAATGCCAAAATGATCTATGCCCGTCACACTTATGCCACATTACGATGAAGATGTATCAAAGCCTTGTGACGCTATAGTCCTATAGGACGATTACCCAACTGGAGAGCGATGTCTCTGCTCTTTTTACGGTCCGAGGGAGTACACTTTGTCGATTAGTGCATGCGCGGAGGAACCAGCCGGTCGGGCTCAGGAAGTCTACATGGATGCCGACG


print(len("CTAATACCCCAGTATCAACTGTCTCATGACACATGAATGCCAAAATGATCTATGCCCGTCACACTTATGCCACATTACGATGAAGATGTATCAAAGCCTTGTGACGCTATAGTCCTATAGGACGATTACCCAACTGGAGAGCGATGTCTCTGCTCTTTTTACGGTCCGAGGGAGTACACTTTGTCGATTAGTGCATGCGCGGAGGAACCAGCCGGTCGGGCTCAGGAAGTCTACATGGATGCCGACG"))


#largestCommonMotif("D:\Programming\Python_code\Rosalind_BioInfo_Challenges\GraphAlgorithms\sampleDataOverlap2.txt", variableLength=True)


# how to make a list of all substrings from a string of a given size? 











