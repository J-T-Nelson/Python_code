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

f = open(, 'r')
fasta = f.read()
f.close()

seqs = fasta.split('>')[11:]

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

profileMat = [[], [], [], []]
transpose = list(zip(*seqs2))
colNum = 0
for row in transpose:
    profileMat[0][colNum] = row.count('A')
    profileMat[1][colNum] = row.count('C')
    profileMat[2][colNum] = row.count('G')
    profileMat[3][colNum] = row.count('T')
    colNum += 1

# need to work out consensus sequence now... 

pMtrans = list(zip(*profileMat))
for row in pMtrans:
    #grab greatest value.. and somehow associate with respective letter? 







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
print(matrix)
print(*matrix)

# Iterate over the columns of the transposed matrix
for col in transposed_matrix:
    print(col)

###### END #############################################
