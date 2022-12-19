# PRETEXT: Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

# Calculating hamming distance between two strings

def hammingDistance(s1, s2):
    if len(s1) != len(s2):
        return(-1)

    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1
    return(dist)


t1 = 'GAGCCTACTAACGGGAT'
t2 = 'CATCGTAATGACGGCCT'

print(hammingDistance(t1,t2))


chal1 = 'TCTATGGATATATGCAGCAGTTCAGACCTCGCCTCGATGTGTCAGCGGGACCCCCTTTGCGCTCACTGCCGTGGAGATAATCCCTCACTACGCATCCTGGGCTCTCCGAGACGCCTATCAGGTTTATCCCGCACTGTATCTGCGTGAGGAGTAGTCTTGACTCATGTGCAACTTCGCTCGACTTACGACGACCAGAGAACTTAACTACCTGGGTGGCGCAGTCCAAGTTATCGTCACATACCTTCACGTCGGAGTTGGCGTGTTCATCATCGGGATTTTATCCGACCGGTGAGAAGTATCGTGCACCGCCCACAGTCTTGCACGATACAAGCATTTAGTGGAGGTAGTCGTCTGAGACACTCACATCTCTATAGTGTCCAAGAATGGCGCCGACCTTTAGGCGGCTTCGTCCGGCGACCGAGGATCTCGATGTAGCACACTCGTCTGGTGGACGGCCGTATGGTATATGTACACTGATGTTTTTGGCTAATGGACATGAAAAACCGTTATTAGGTGCCCCTCTTGCGCGGTAGGTTGGAAACAGTTTAACATTCTAAGGAGTTTGTTACCCTGGTTCACGTCGCGAGCGGTTTCTGAGAGTTTGTGTTGCTGTGCGTTTGTGGACTTCGACTATTTTTCGCGCTGCTCCATCATAGCCAACACGAGCTCATTGCAAGCAATTGTGTTTAGTCTCAGCTGTAGGATCATGTGCGAGTGGCGGGTTTAAAACTGAATCCCGTTAGGACACTCTGTGGCACACGGCTGCAGGCCTCGAACAGGTCGACCCACGGTTGAGTCTTGCCGCTGGTTCATCCTGCCACTTGAATTACTCCTGTGGGGCCGGGAGCAGAGACAGGGTCCTCCTATTACATTGGTAGTCTACGAAACCCCGAGTTGGTTCCCAAGATCACCTGGCTGTGACCCAATCGTCGCAGATTGCAAGGCTACGATGGAACTAAACCCCTACAAGGC'

chal2 = 'TCTATCCGAATATAAAGATGTCCACGACGCCTATTTATGTGGCACCCTCAACCACCCGGCTGTCGCACATGCCGTGACCATTTCTTTAGTCGCATCCTGTGTTAACCAGCAGGCTCTTCAGGGCAAGCCATCAGTTAATACGGTTGACTACCTGACTTGACTTCAGTGGATCATCGCCGGACTTCCGACGACCCTAGTACTGCAGTACATGGTAGCGGACGTCCCGTTTATCCTCAACCAAGGGCACGTCAAAGCTGTCGCGACAGTCGGCGCGAATTAGGGAACCAAGTGGCAAACATCTGGATTGGCACACAAGCTTGGAGTATACCCGGCTTCTGATGTTTTAGGTGTGTGCCAAACTCTTCGCACTATCGGGATCGATACAATAAGGGATCGATGGGCGGGATGGGCCTGCGTTTCAGAGGCCCGAGATGGGGTCCTTCACCTGTGCACGGCCGCTACAATTTAGTTACGCGGCGTTTGGTACGATCGGACGCGAAAGACCTAAGTCAAGTGCCTCCTTGGCGTGGGAAGATGTACACTGACGACAAGCCTCAGCAGCTAGTTTCAATGTGCGGTCTGACGAGCGGCTCCAGCAAGTCGGTCTAGGTAGGCACTAGCGATATGCCCTTAGTATGCTCGTTAAGGCTTCGCAGAGCAAACTTGCACCTTGCAAGCCGTTGCGTTTCAGCTCATCTGCATGGTCAATTTCGTTTATTGAATGGGAGAATGAAGAGTACAACAACTCTTTGTTCTAGAGGGTGGCATGTCAAAAACAGGTCGATCTACGGTTTTGTCTTACAGCAGCCTCTTACGGGTAATTGCATAGCCCTCTATCGGATTCCCGGATCCAGTGGGTCCACCTCTTAAATCAGAAGAATGAACAGATCAGAGTAAATTCCCAACACCAGCAGGCTGTGACCCAAGCCTCGGAGTATGCAAAGCGTGAACCAAGTGAAATCAACATGTGCC'

print(hammingDistance(chal1, chal2))

# REFLECTION: This challenge was quite easy. I do wonder if there is a more efficient means of solving the problem though. I also wonder if I didn't consider any obvious issues with my script. 
# I believe you cannot avoid making 1 comparison for each respective position in the two strings.. its the nature of this measurement, thus I don't know if an algorithm can get more efficient for this, only hardware can / the software speaking to the hardware. 

