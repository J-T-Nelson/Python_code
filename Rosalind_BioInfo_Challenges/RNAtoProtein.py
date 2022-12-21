# straightforward exercise, however I want to do it as well as possible. 

# We need a dictionary which contains the full coodon table within 
#  first I need to scan for the start codon, then truncate anything to the left of that string provided. 
#  then I need to slice the remaining string into a list of 3-length strings, which will be processed as keys of the dict thus retreiving the proper protein symbol. 

# questions, how to scan a string for the first occurrence of a sequence? 
#    2. how to slice into 3 length? 

def rna2Protein(mRNA):

    codonDict = {
        'UUU' : 'F'   ,   'CUU' : 'L',      'AUU' : 'I',      'GUU' : 'V',
        'UUC' : 'F'   ,   'CUC' : 'L',      'AUC' : 'I',      'GUC' : 'V',
        'UUA' : 'L'   ,   'CUA' : 'L',      'AUA' : 'I',      'GUA' : 'V',
        'UUG' : 'L'   ,   'CUG' : 'L',      'AUG' : 'M',      'GUG' : 'V',
        'UCU' : 'S'   ,   'CCU' : 'P',      'ACU' : 'T',      'GCU' : 'A',
        'UCC' : 'S'   ,   'CCC' : 'P',      'ACC' : 'T',      'GCC' : 'A',
        'UCA' : 'S'   ,   'CCA' : 'P',      'ACA' : 'T',      'GCA' : 'A',
        'UCG' : 'S'   ,   'CCG' : 'P',      'ACG' : 'T',      'GCG' : 'A',
        'UAU' : 'Y'   ,   'CAU' : 'H',      'AAU' : 'N',      'GAU' : 'D',
        'UAC' : 'Y'   ,   'CAC' : 'H',      'AAC' : 'N',      'GAC' : 'D',
        'UAA' : 'Stop',   'CAA' : 'Q',      'AAA' : 'K',      'GAA' : 'E',
        'UAG' : 'Stop',   'CAG' : 'Q',      'AAG' : 'K',      'GAG' : 'E',
        'UGU' : 'C'   ,   'CGU' : 'R',      'AGU' : 'S',      'GGU' : 'G',
        'UGC' : 'C'   ,   'CGC' : 'R',      'AGC' : 'S',      'GGC' : 'G',
        'UGA' : 'Stop',   'CGA' : 'R',      'AGA' : 'R',      'GGA' : 'G',
        'UGG' : 'W'   ,   'CGG' : 'R',      'AGG' : 'R',      'GGG' : 'G' 
    }
    codingRNA = mRNA[mRNA.find('AUG'):] #finding start codon and subsetting the string in at that point

    s = 0
    e = 3
    proteinSeq = ''
    for i in range(len(codingRNA)//3): #for each 3 length substring add an amino acid to the protein being built 
        codon = codingRNA[s:e]
        s+=3
        e+=3

        if(codonDict[codon] == 'Stop'):
            break

        proteinSeq += codonDict[codon]
    return(proteinSeq)

##### EXPERIMENTING ###########################################
s = 'naglkgndjouesssfoj'

sA = s[::3]
print(sA)

sA2 = s[0:3]
print(sA2)

#Answer to Question 2: 
strt = 0
end = 3
for i in range(len(s)//3):
    print(s[strt:end])
    strt+=3
    end+=3
################################################


print(range(len(s)//3))

# answer to question 1: 
es = s[s.find('gnd'):]
print(es)
###### END ##########################################

testSeq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

print(rna2Protein(testSeq))
print(rna2Protein(testSeq) == 'MAMAPRTEINSTRING') # True .... Success

chalFile = open("C:\\Users\\Tanner_N\\Downloads\\rosalind_prot.txt", 'r')
chalSeq = chalFile.read()
chalFile.close()

print(rna2Protein(chalSeq)) # NICE got the right answer first try! 



# cool alternative solution

string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

coded = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
decoded = ''

traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2])) #efficient means of making a dictionary of the regularly formatted table. 

for i in range(0, len(coded)-3, 3):
    decoded += traDict[coded[i:i+3]] # this solution is not general, as it cannot deal with sequences where the start and end arent literally decided already, however I suppose you can always write a helper function which would ensure the regularity of strings going in which thus would allow for more general use of this script. 

print(decoded)