# will also put notes in here about graph work in python... so this is the learning space which can remain separate from the solutions to problems themselves! 

# def - OVERLAP GRAPH - An overlap graph is a directed graph in which each string in a collection is represented by a node and node s is connected to t with a directed edge if some suffix of s equals a prefix of t.
 # - We assume that the two substrings are longer than some predetermined threshold k to prevent noise in the graph.


stest = 'GGGTGGGHIG'
print(stest[:3])
print(stest[-3:])


# having issues appending a list to an empty list.... 

el = []
list1 = ['dog', 'cat']
list2 = ['doggg', 'catss']

print(el)

el.append(list1)
el.append(list2)
print(el) # no issues adding lists to a list this way

el.append(['ham', 'beast']) # again this appends just fine. no issues
print(el)



# Dirty soltion: 
def overlapAdjacencyList(filePath, k = 3):

    f = open(filePath, 'r')
    seqs = f.read().split('>')[1:]
    f.close()

    print(seqs)
    
    # nodeDict = {}
    # for s in seqs:
    #     components = s.split('\n')
    #     print(components)
    #     nodeDict[components[0]] = components[1]

    # print(nodeDict)    

    key = []
    val = []
    for s in seqs:
        components = s.split('\n')
        key.append(components[0])
        val.append(components[1])
    print(key)
    print(val)
    print(val[1])
    print(val[1][:3])
    # check prefixes all the way down, then suffixes all the way down for all possible combinations
    # add matches to a list of lists. then process that list of lists for the desired output


    adjacencyList = []
    dictLength = len(key)
    for ind in range(dictLength):
        #print(ind)
        for pair in range((ind+1), dictLength):
            print(pair)
            #print(nodeDict[pair]) # cannot access dict elements by index... dicts are unordered ... I changed my data structure to two arrays! so indexing and ordering is supported now 
            if val[ind][:k] == val[pair][-k:]: #adding prefix to suffix match for current ind sequence in val[]
                adjacencyList.append([key[ind], key[pair]])
            
            if val[ind][-k:] == val[pair][:k]: #adding suffix to prefix match for current ind sequence in val[]
                # print("priting 'pair' " + str(pair))
                # print("priting 'ind' " + str(ind))
                # print("What is the type of this shit? " + str(type(ind)) + " " + str(type(pair)))
                adjacencyList.append([key[ind], key[pair]])
                
        print("THIS IS THE CURRENT ind VALUE: " + str(ind))
        print(adjacencyList)



# Saving my notes on an issue I had... 
fileOut = open('D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\GraphAlgorithms\\OLgraphAnswer.txt', 'w') # we are getting permissions issues writting to this folder for some reason.. windows weirdness. Going to forgo that sort of answer right now as its a bit too much of a rabbit hole to solve. Changing permissions using bash is ineffective. Changing permissions using manual modification by GUI options is also ineffective. Windows just secretly switches things back with no messages or anything, thus making file permissions inaccessible to the uninitiated windows user. 
    # FIXED ... not sure if this was the issue all along.. I may have just had the wrong address entered... I really need to ALWAYS check that the address is 100% correct before troubleshooting further.. I should take the time to make some basic troubleshooting flowcharts or to find some online to learn from for these basic computer and programming issues. 



# OLD ANSWER USING SETS: 

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
            
            if val[ind][-k:] == val[pair][:k]: #adding suffix to prefix match for current ind sequence in val[]
                adjacencyList.append([key[ind], key[pair]])

            if val[ind][:k] == val[pair][-k:]: #adding prefix to suffix match for current ind sequence in val[]
                adjacencyList.append([key[pair], key[ind]])

    #printing solution: 
    fileOut = open('D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\GraphAlgorithms\\OLgraphAnswer.txt', 'w') 
    answerSet = set() # making empty set datastructure
    for e in adjacencyList: # UPDATE.... Not sure if this set DS is actually useful anymore... I think it may have only been useful because I was adding duplicates due to an error in my code.. since each pairwise comparison only happens once though, unless there are non-unique entries in the data in would this step be necessary to remove such dupolicate entries in the answer set... we would be wise to simply filter the data in for duplicate values in the case we believed data in had such qualities. 
        solutionLine = str(e).replace('[', '').replace(']', '').replace(',','').replace("'", '') 
        answerSet.add(solutionLine)
    
    for e in answerSet: # printing the answer set in desired format
        line = e.replace("'", '')
        print(line)
        fileOut.write(line + "\n")
    fileOut.close()

overlapAdjacencyList('D:\Programming\Python_code\Rosalind_BioInfo_Challenges\GraphAlgorithms\sampleDataOverlap2.txt')