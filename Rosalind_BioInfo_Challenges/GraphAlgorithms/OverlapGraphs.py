

# so we are constructing an adjacency list which pairs each suff/pre overlap from a set of strings (each a node in their conceptual representation) as an edge.
#  our function should take in a k value, which is the number of characters needed for a suffix / prefix to be considered overlapping. Obviously a k of 1 would make MANY things overlap which would result in a very noisy set of edges that isn't very informative in the context of sequence alignment



def overlapAdjacencyList(filePath, k = 3, fOutName = "OLgraphAnswer.txt", debugPrint=False):

    f = open(filePath, 'r')
    seqs = f.read().split('>')[1:]
    f.close()
    #print(seqs)
    
    key = []
    val = []
    for s in seqs:
        key.append(s[:13])
        val.append(s[14:].replace('\n',''))
    
    if debugPrint:
        print("Key:", key)
        print("Val:", val)
    # check prefixes all the way down, then suffixes all the way down for all possible combinations
    # add matches to a list of lists. then process that list of lists for the desired output
    adjacencyList = []
    dictLength = len(key)
    for ind in range(dictLength):
        for pair in range((ind+1), dictLength):
            
            if val[ind][-k:] == val[pair][:k]: #adding suffix to prefix match for current ind sequence in val[]
                adjacencyList.append([key[ind], key[pair]])

            if val[ind][:k] == val[pair][-k:]: #adding prefix to suffix match for current ind sequence in val[]
                adjacencyList.append([key[pair], key[ind]])

    #printing solution: 
    exportFileName = "D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\GraphAlgorithms\\" + fOutName
    fileOut = open(exportFileName, 'w') 
    for e in adjacencyList: # printing the answer set in desired format
        line = str(e).replace("'", '').replace('[','').replace(']','').replace(',','')
        print(line)
        fileOut.write(line + "\n")
    fileOut.close()

overlapAdjacencyList('D:\Programming\Python_code\Rosalind_BioInfo_Challenges\GraphAlgorithms\sampleDataOverlapGraph.txt')
overlapAdjacencyList('D:\Programming\Python_code\Rosalind_BioInfo_Challenges\GraphAlgorithms\sampleDataOverlap2.txt', fOutName="OL2SampleOut.txt", debugPrint=True)
overlapAdjacencyList('D:\Programming\Python_code\Rosalind_BioInfo_Challenges\GraphAlgorithms\sampleDataOverlap3.txt', fOutName="OL3SampleOut.txt")

print("")


#overlapAdjacencyList("C:\\Users\\Tanner_N\\Downloads\\rosalind_grph (1).txt")
#overlapAdjacencyList("C:\\Users\\Tanner_N\\Downloads\\rosalind_grph (4).txt")
overlapAdjacencyList("C:\\Users\\Tanner_N\\Downloads\\rosalind_grph (5).txt", fOutName="OLgraphAttempt5.txt")


# MY MAIN ISSUE WAS JUST IN THE INITIAL INGESTION OF DATA... I FORGOT TO CONSIDER THEM PUTTING UNNECESSARY NEW LINES ALL OVER THE PLACE BECAUSE IT WASN"T EVIDENT IN THE SAMPLE INPUT. FOR THE FUTURE... I THINK YOU JUST HAVE TO BE AWARE OF WHAT ASSUMPTIONS YOU CAN AND CANNOT MAKE... AND WHEN FAILING, LOOKING AT DIFFERENCES IN THE SAMPLE PROVIDED AND ACTUAL DATA FOR DIFFERENECES WHICH MAY CREATE ISSUES.. I totally lost my patience on this problem though, as my logic was pretty sound from the get go, and very little issues in my process were where I was wrong, and finding other sample data to help identify kinks was far too difficult to seek out. 

# overlapAdjacencyList("C:\\Users\\Tanner_N\\Downloads\\rosalind_grph.txt") # failure... non-unique answers are being produced. May want to use a set to get rid of non-uniques then get the output of the set formatted properly. 
    
#overlapAdjacencyList("C:\\Users\\Tanner_N\\Downloads\\rosalind_grph (1).txt") # still getting the wrong answer even with only unique answers in the set... kind of mentally distracted due to the issues with writting a fucking file where I want on my own fucking system. It is pretty obscene how difficult it is to be able to do something so simple. 
 # maybe the incorrect answer is related to the unordered iteration occuring with a set being processed? 

 # NEXT TIME... READ THROUGH SOME OF THE FORUM POSTS DETAILING WHAT ERRORS MAY HAVE GONE WRONG IN THIS PROBLEM ... I WAS A BIT DISTRACTED BY OTHER THOUGHTS AND THINGS DURING THIS SESSION AND DIDN"T THINK TOO DEEPLY ABOUT POSSIBLE ISSUES I WOULD ENCOUNTER BUT HAVE A NICE SCAFFOLD OF A SOLUTION PREPARED. 


# Testing for duplicate values in data in... 

def testDupes(fileIn, printStatements = False):
    f = open(fileIn, 'r')
    fCont = f.read().split('>')[1:]
    f.close()
    if printStatements:
        print(fCont)

    fCont = [entry[:13] for entry in fCont]
    if printStatements:
        print(fCont)
    
    contSet = {e for e in fCont}

    #dupeIndicate = True
    if len(contSet) == len(fCont):
        print("All entries unique in: ", fileIn)
    else:
        print("Duplicate entrys exist in: ", fileIn)

def testDupesList(fileIn, printStatements = False):
    f = open(fileIn, 'r')
    fCont = f.read().split('\n')
    f.close()
    if printStatements:
        print(fCont)
    
    contSet = {e for e in fCont}
    if printStatements:
        print(contSet)
    #dupeIndicate = True
    if len(contSet) == len(fCont):
        print("All entries unique in: ", fileIn)
    else:
        print("Duplicate entrys exist in: ", fileIn)


# testDupes("C:\\Users\\Tanner_N\\Downloads\\rosalind_grph (1).txt") # nice I am getting the desired subset! 
# testDupes("C:\\Users\\Tanner_N\\Downloads\\rosalind_grph.txt") 

# testDupesList("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\GraphAlgorithms\\OLgraphAnswer.txt")



