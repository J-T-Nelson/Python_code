



# DEF: Profile Matrix - A matrix encoding the number of times that each symbol of an alphabet occurs in each position from a collection of strings 
 #  so a profile matrix in other words counts the number of times a nucleotide (or other symbol) occurs in a given column. ... and likely would represent the amount as a percentage of the total rows with a given character

# so we are given a fasta file with a bunch of DNA sequences... and we want to create a profile matrix as well as a consensus sequence. 
# STRATEGY: 
""" parse out nucleotide sequences from file.
    - put each into a list
    - process the list to create the profile matrix
    - process the profile matrix to create the consensus string
    - return all valid consensus sequences 
"""

# QUESTIONS: 
""" - How are matrices represented in Python? 
    - is there any reason to not just use a list or dict to represnt my profile matrix? (considering I just need to output a text version of it anyway?)
"""

# f = open(, 'r')
# fasta = f.read()
# f.close()

# seqs = fasta.split('>')[11:]

testData = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

seqs = testData.split('>')[1:] # <- was confused when subsetting this ... but since its an array, subsetting is subsetting elements of the array.. not subsetting elements in the array... so [11:], says grab the 12th element of the array and everything else.. not the 12 element of each string in the array... 
# print(seqs)
# print(seqs[1])
# print(seqs[1:])
# print(seqs[11:])

seqs2 = []
for s in seqs:
    seqs2.append(s[11:].replace('\n', '')) # DNA seqs are now in seqs2
    #s = s[11:].replace('\n', '')
    #seqs[s] = s # this is invalid as I thought, still not sure how to keep a counter without just writing one in yet. 
print(seqs2)
#print(*seqs2)
#print(type(seqs2[0]))

eArray = [0] * len(seqs2[0])
profileMat = [eArray, eArray, eArray, eArray] # empty arrays cannot have values assigned to them by position, positional assignment can only occur for positions which already are extant for an array. 
transpose = list(zip(*seqs2))
colNum = 0
print("PRINTING TRANSPOSE: " + str(transpose))

# SECOND APPROACH ... PACKAGING APPROACH 1 and 2 together for speed
A = []
C = []
G = []
T = []

for row in transpose:
    profileMat[0][colNum] = row.count('A')
    print(profileMat)
    profileMat[1][colNum] = row.count('C')
    print(profileMat) # printing shows that each array is getting the same value appended at the same time... so I am not properly referencing the positions in my 2D array
    profileMat[2][colNum] = row.count('G')
    profileMat[3][colNum] = row.count('T')
    
    colNum += 1
    A.append(row.count('A'))
    C.append(row.count('C'))
    G.append(row.count('G'))
    T.append(row.count('T'))

print(str(A) + '\n' + str(C) + '\n' + str(G) + '\n' + str(T)) # beautiful! 
# need to work out consensus sequence now... 

pMtrans = list(zip(*profileMat))
conSeq = ''
for row in pMtrans:
    #grab greatest value.. and somehow associate with respective letter? 
    # each row of pMtrans is a col of the profile matrix. position 0 = A, 1 = C, 2 = G, 3 = T

    # need to check which position has the greatest value and add a letter to conSeq depending on which position has the greatest value. 
    pass


print(profileMat)
print(pMtrans)





###### EXPERIMENTING ####################################### 
# eD = {}
# eD[str(0)] +=1
# print(eD)

eD = {}
eD[str(0)] = 0
eD[str(0)] +=1
print(eD) # dict value must be initialized at 0 before incrementing up! 


# to use for loops to count occurrences of letters at specific positions could be ugly... a dict would clean it up a bit I think.. but we may need several dicts... I think if we could actually have a matrix data structure that may be most elegant though. 
colNumj = 0
dictList = [{},{},{},{}]
#OR
A, C, G, T = {}, {}, {}, {}
dL = []
for seq in seqs2:
    cntr = 0
    for char in seq:
        if char == 'A':
            A[str(cntr)] = 0 # starting to see how annyoing it will be to use dictionaries like this... I think directly treating the list of arrays as a matrix to produce another matrix will be much more efficient and writable 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transpose the matrix using zip()
transposed_matrix = list(zip(*matrix))

#see what *matrix do :: `*` is used to unpack elements of a list. It is thus commonly used to pass multiple arguments to functions by unpacking a list as multiple arguments to a function. 
#print(matrix)
#print(*matrix)

# Iterate over the columns of the transposed matrix
# for col in transposed_matrix:
#     print(col)

###### END #############################################



eArray = [0] * len(seqs2[0])
profileMat = [eArray, eArray, eArray, eArray] # empty arrays cannot have values assigned to them by position, positional assignment can only occur for positions which already are extant for an array. 
transpose = list(zip(*seqs2))
colNum = 0
for row in transpose:
    profileMat[0][colNum] = row.count('A')
    print(profileMat)
    profileMat[1][colNum] = row.count('C')
    print(profileMat) # printing shows that each array is getting the same value appended at the same time... so I am not properly referencing the positions in my 2D array
    profileMat[2][colNum] = row.count('G')
    profileMat[3][colNum] = row.count('T')


# HOW TO PROPERLY REFERENCE POSITIONS IN A 2D array? 

eArray = [0] * len(seqs2[0])
profileMat = [eArray, eArray, eArray, eArray] # both profileMat and eArray refer to the same inner list object, so when you modify an element of the inner list using either profileMat or eArray, the change is reflected in both variables. 

profileMat = [[0] * len(eArray) for _ in range(4)] # <- this is a list comprehension which will produce unique sub arrays within profileMat. I suppose this is a matter of referencing and copying and recognizing that while it is not intuitive, inserting the same array into a super array many times actually is just putting pointers to the same spot in memory within that super array multiple times. 

print(profileMat)

profileMat[0][1] = 20 # this assigns the 2nd col of ALL elements in the array to 20 

print(profileMat)
profileMat[0] = 20
print(profileMat)
print(profileMat[0])
print(profileMat[1])
print(profileMat[1][2]) # this does in fact draw out the element in the 2nd row and 3rd col ... so why cant I assign that specific value through the same referencing syntax? 





# TROUBLE SHOOTING: For a general solution, we must detect the first point of actual nucleotide strings accurately regardless of the preceding text for each individual sequence taken in.. so we will not assume they all start at the same position, but instead will dynamically check each sequence taken in. 
# this approach is more computationall expensive, but logistically more robust. 

# I think there are a number of ways to check for the beginning of our string... the best most simple rule that is still general is what I want. 
# I think a sufficiently general solution may be to check for the first instance of a character 'A','C','G','T', then find the following two characters and ensure they too belong to that set.. if that is the case then we know from the first point checked we have a sequence starting and can discard everything else before that point. 

# to execute we need a set which we can check membership against, a startingPos variable, and an while loop which executes until it finds a valid starting position... 

# A separate, perhaps more efficient solution would be to simply enter the value where sequences will be starting for each seq... this requires standardization of intput.. which is a safe assumption to make in any sofisticated data pipeline

ss = "Rosalind_3487\nT"
ss2 = "Rosalind_3\nT"

print(ss[11:] + "\n" + ss2[11:])

print(ss[13:] + "\n" + ss2[11:])

print(ss[14:] + "\n" + ss2[11:])

print(ss[15:] + "\n" + ss2[11:]) # ok... as I should know, the escape character isn't indexed in a string being subset. Therefore, to move past it, you only need 1 advance of the index, not 2. ( I am not sure if its the '\' or the 'n') which is indexed... I think its actually the combination tbh.. as the conbination represents the meaning which will be interpreted, which is that [ '\n' == 'carridge return' == "the enter key" ] 

# ADDING THE SEQ START PARAMETER IS CERTAINLY A NICE WAY TO SOLVE FOR THE DYNAMIC INPUT ISSUE WITHOUT ADDING COMPUTATIONAL COMPLEXITY... logistical complexity has been added however! 