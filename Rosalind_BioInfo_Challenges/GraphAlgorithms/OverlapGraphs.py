

# so we are constructing an adjacency list which pairs each suff/pre overlap from a set of strings (each a node in their conceptual representation) as an edge.
#  our function should take in a k value, which is the number of characters needed for a suffix / prefix to be considered overlapping. Obviously a k of 1 would make MANY things overlap which would result in a very noisy set of edges that isn't very informative in the context of sequence alignment



def overlapAdjacencyList(filePath, k = 3):

    f = open(filePath, 'r')
    seqs = f.read().split('>')[1:]
    f.close()
    #print(seqs)
    
    key = []
    val = []
    for s in seqs:
        components = s.split('\n')
        key.append(components[0])
        val.append(components[1])
    
    # check prefixes all the way down, then suffixes all the way down for all possible combinations
    # add matches to a list of lists. then process that list of lists for the desired output
    adjacencyList = []
    dictLength = len(key)
    for ind in range(dictLength):
        for pair in range((ind+1), dictLength):

            if val[ind][:k] == val[pair][-k:]: #adding prefix to suffix match for current ind sequence in val[]
                adjacencyList.append([key[ind], key[pair]])
            
            if val[ind][-k:] == val[pair][:k]: #adding suffix to prefix match for current ind sequence in val[]
                adjacencyList.append([key[ind], key[pair]])

    #printing solution: 
    fileOut = open('D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\GraphAlgorithms\\OLgraphAnswer.txt', 'w') # we are getting permissions issues writting to this folder for some reason.. windows weirdness. Going to forgo that sort of answer right now as its a bit too much of a rabbit hole to solve. Changing permissions using bash is ineffective. Changing permissions using manual modification by GUI options is also ineffective. Windows just secretly switches things back with no messages or anything, thus making file permissions inaccessible to the uninitiated windows user. 
    # FIXED ... not sure if this was the issue all along.. I may have just had the wrong address entered... I really need to ALWAYS check that the address is 100% correct before troubleshooting further.. I should take the time to make some basic troubleshooting flowcharts or to find some online to learn from for these basic computer and programming issues. 

    answerSet = set() # making empty set datastructure
    for e in adjacencyList:
        solutionLine = str(e).replace('[', '').replace(']', '').replace(',','').replace("'", '') 
        answerSet.add(solutionLine)
    
    for e in answerSet: # printing the answer set in desired format
        line = e.replace("'", '')
        print(line)
        fileOut.write(line + "\n")
    fileOut.close()

overlapAdjacencyList('D:\Programming\Python_code\Rosalind_BioInfo_Challenges\GraphAlgorithms\sampleDataOverlapGraph.txt')

print("")

# overlapAdjacencyList("C:\\Users\\Tanner_N\\Downloads\\rosalind_grph.txt") # failure... non-unique answers are being produced. May want to use a set to get rid of non-uniques then get the output of the set formatted properly. 
    
#overlapAdjacencyList("C:\\Users\\Tanner_N\\Downloads\\rosalind_grph (1).txt") # still getting the wrong answer even with only unique answers in the set... kind of mentally distracted due to the issues with writting a fucking file where I want on my own fucking system. It is pretty obscene how difficult it is to be able to do something so simple. 
 # maybe the incorrect answer is related to the unordered iteration occuring with a set being processed? 

 # NEXT TIME... READ THROUGH SOME OF THE FORUM POSTS DETAILING WHAT ERRORS MAY HAVE GONE WRONG IN THIS PROBLEM ... I WAS A BIT DISTRACTED BY OTHER THOUGHTS AND THINGS DURING THIS SESSION AND DIDN"T THINK TOO DEEPLY ABOUT POSSIBLE ISSUES I WOULD ENCOUNTER BUT HAVE A NICE SCAFFOLD OF A SOLUTION PREPARED. 