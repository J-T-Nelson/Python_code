



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

transpose = list(zip(*seqs2))
print("PRINTING TRANSPOSE: " + str(transpose))

A = []
C = []
G = []
T = []
for row in transpose:
    A.append(row.count('A'))
    C.append(row.count('C'))
    G.append(row.count('G'))
    T.append(row.count('T'))

#print(str(A) + '\n' + str(C) + '\n' + str(G) + '\n' + str(T)) # beautiful! 
# need to work out consensus sequence now... 
 # if there are multiple consensus strings due to ties in consensus characters at a given position I think we should just store the fact that there are multiple consensus sequences. The current problem doesn't require we store all of them, rather that we just get a single valid consensus string. 

profileMat = [A,C,G,T]
pMtrans = list(zip(*profileMat))
conSeq = ''
pos = -1 
for row in pMtrans:
    # each row of pMtrans is a col of the profile matrix. position 0 = A, 1 = C, 2 = G, 3 = T
    consMax = max(row)
    pos+=1
    if A[pos] == consMax:
        conSeq += 'A'
        continue
    if C[pos] == consMax:
        conSeq += 'C'
        continue
    if G[pos] == consMax:
        conSeq += 'G'
        continue
    if T[pos] == consMax:
        conSeq += 'T'
        continue

print(conSeq)
print("A: " + str(A) + '\n' + "C: " +  str(C) + '\n' + "G: " + str(G) + '\n' + "T: " + str(T)) # beautiful! 



# ok my code works for the practice example. Now to wrap things in a function which can take a file in and produce the desired output. 

def consAndProfile(filePath, seqStart = 11, debugPrinting = False):
    # grabbing sequences as arrays from file
    f = open(filePath, 'r')
    seqs = f.read().split('>')[1:] 
    f.close()

    seqs2 = []
    for s in seqs:
        seqs2.append(s[seqStart:].replace('\n', '')) # DNA seqs are now in seqs2

    if debugPrinting:
        print(seqs2) # printing for debugging

    # setting up profile matrix for DNA sequences
    transpose = list(zip(*seqs2))

    if debugPrinting:
        print("printing Transpose:") # debug printing
        print(transpose)

    A = []
    C = []
    G = []
    T = []
    for row in transpose: #row of the transpose is a col of the original matrix (which in this case is a non-native representation of the list seqs2 )
        A.append(row.count('A'))
        C.append(row.count('C'))
        G.append(row.count('G'))
        T.append(row.count('T'))

    profileMat = [A,C,G,T]

    # determining one single consensus sequence
    pMtrans = list(zip(*profileMat))
    conSeq = ''
    pos = -1 
    for row in pMtrans:
        # each row of pMtrans is a col of the profile matrix. position 0 = A, 1 = C, 2 = G, 3 = T
        consMax = max(row)
        pos+=1
        if A[pos] == consMax:
            conSeq += 'A'
            continue
        if C[pos] == consMax:
            conSeq += 'C'
            continue
        if G[pos] == consMax:
            conSeq += 'G'
            continue
        if T[pos] == consMax:
            conSeq += 'T'
            continue

    #printing results:
    print(conSeq)
    print("A: " + str(A).replace('[', '').replace(']', '').replace(',', '') + '\n' + 
          "C: " + str(C).replace('[', '').replace(']', '').replace(',', '') + '\n' + 
          "G: " + str(G).replace('[', '').replace(']', '').replace(',', '') + '\n' + 
          "T: " + str(T).replace('[', '').replace(']', '').replace(',', ''))
    outputFile = open('D:/Programming/Python_code/Rosalind_BioInfo_Challenges/StringAlgorithms/consOutput.txt', 'w')
    outputFile.write(conSeq + '\n')
    outputFile.write('A: ' + str(A).replace('[', '').replace(']', '').replace(',', '') + '\n')
    outputFile.write('C: ' + str(C).replace('[', '').replace(']', '').replace(',', '') + '\n')
    outputFile.write('G: ' + str(G).replace('[', '').replace(']', '').replace(',', '') + '\n')
    outputFile.write('T: ' + str(T).replace('[', '').replace(']', '').replace(',', '') + '\n')

    # printing validation stats: 
    if debugPrinting:
        if len(conSeq) == len(seqs2[1]):
            print("Length of conSeq == length of Sequences")
        else:
            print("Length of conSeq != length of Sequences")
    






# TEST RUN OF FUNC: 



# functions works so far... so lets test it on the real prob now. 

consAndProfile("C:\\Users\\Tanner_N\Downloads\\rosalind_cons (1).txt", 14)

consAndProfile('D:/Programming/Python_code/Rosalind_BioInfo_Challenges\\StringAlgorithms\\consTestFile.txt') # seems only full path referencing is working.... probably because I am running the terminal in R_projects for some reason... idk 

consAndProfile("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\ConsensusAndProfileTestData2.txt") # this is solving correctly.. however I am still failing on the data from rosalind.. 


consAndProfile("C:\\Users\\Tanner_N\Downloads\\rosalind_cons (3).txt", 14) # finally SUCCESS!! ... I was just not formatting my output exactly as they were.. not removing certain characters which I didn't recognize as significant.. 



