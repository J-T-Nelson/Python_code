

def findSubStringsL(majorString, minorString):

    index = 0
    indList = []
    while True:
        index = majorString.find(minorString, index) # second argument must specify the index to start at 
        if index == -1:
            break

        index += 1
        indList.append(index)
        
    return(indList)


def findSubStringsS(majorString, minorString):

    index = 0
    indString = ''
    while True:
        index = majorString.find(minorString, index) # second argument must specify the index to start at 
        if index == -1:
            break
        
        index += 1
        indString += str(index)+' '
        
    return(indString)


###### EXPERIMENTING ####################################### 
s = "Hello I am Jawn"

ind = s.find("I", 10)
ind2 = s.find("I")

print("ind: " + str(ind)) # -1
print("ind2: " + str(ind2)) # 6 .... confirmed the function of the second arg. 
###### END #############################################

print(findSubStringsL("GATATATGCATATACTT", "ATAT"))
print(findSubStringsS("GATATATGCATATACTT", "ATAT")) # sweet this gets the good answer 

f = open("C:\\Users\\Tanner_N\\Downloads\\rosalind_subs.txt", 'r')
chalStrings = f.read().split()
f.close()

print(findSubStringsS(chalStrings[0], chalStrings[1])) # success! 