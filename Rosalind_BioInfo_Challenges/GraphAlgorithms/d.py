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
    fileOut = open('D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\GraphAlgorithms\\OLgraphAnswerFROM_D.txt', 'w') 
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