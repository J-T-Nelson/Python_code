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