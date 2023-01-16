# some remarkably different algorithms were used to solve this problem by others. My solution was a brute force solution that ultimately did a pretty good job at finding the desired result within the given time (2/5ths of the time was used) But other algs seem to outperform my approch by MANY fold, and thus I think its worth consider just how they achieve this. 
# this algorithm is an iterative improvement on someone else's code, where the core principle is to use binary search against string lengths to identify the largest string in a substantially reduced time frame. So if we search the half way length point first, we can know to look at the lengths that are larger or smaller depending on our result... following binary search thus reduces the search time for this task substantially. 

#to get this to work I think I just need to enter the sequences in... 



def prepSeqs(filePath):
    f = open(filePath, 'r')
    fCont = f.read().split(">")[1:]
    f.close()
    fCont = [seq[13:].replace("\n", '') for seq in fCont]
    return fCont


######----- RandalTyers Code -----####################################### 
# "binary search"
# edited version of code by Petar Ivanov
# changes: 
#    rationalized variable names
#    part in seq rather than seq.find(part)==-1     <--- good
#    merged substr_in_all() into common_substr()    <--- good
#    extract seq_0 from seqs                <--- very good

# return first substring of given length that is found in all sequences?
def common_substr(seq_0, seqs, length):
    # look at all possible substrings of a given 'length' 
    length = int(length)
    for start in range(len(seq_0) - length + 1):
        part = seq_0[start:start+length]

        # as soon as you find a sequence that doesn't contain this substring move on to the next substring
        # otherwise return this substring
        # note: indicates that there is at least one common substring of this length
        for seq in seqs:
            if part not in seq:
                break
        else:
            return part
    return ""

def longest_common_substr(seqs):
    # pop seq_0 to reduce number of sequences to search and eliminate need to re-extract each time 
    seq_0 = seqs.pop(0)

    ## starting points for the bounds on the longest common substring used in the binary search ##
    left = 0
    # +1 added to allow entire sequence to be the longest common substring 
    right = len(seq_0) + 1

    # repeat until left and right are adjacent              
    #     use left + 1, because you've already eliminated the right most and you get an endless loop otherwise ...
    while left + 1 < right:
        # pick midpoint in lengths -- nb:  assumes integer math
        mid = (left + right) / 2

        # if any substring of length mid is common to all sequences 
        #    look for substrings of this length or longer
        # otherwise look for substrings of this length or less
        if common_substr(seq_0, seqs, mid) != "":
            left = mid
        else:
            right = mid

    return common_substr(seq_0, seqs, left)



#seqs_1 = prepSeqs("C:\\Users\\Tanner_N\\Downloads\\rosalind_lcsm (1).txt")
# print(seqs_1) # looks good. 

# lcss = longest_common_substr(prepSeqs("C:\\Users\\Tanner_N\\Downloads\\rosalind_lcsm (1).txt"))
# print(lcss) #CTAATACCCCAGTATCAACTGTCTCATGACACATGAATGCCAAAATGATCTATGCCCGTCACACTTATGCCACATTACGATGAAGATGTATCAAAGCCTTGTGACGCTATAGTCCTATAGGACGATTACCCAACTGGAGAGCGATGTCTCTGCTCTTTTTACGGTCCGAGGGAGTACACTTTGTCGATTAGTGCATGCGCGGAGGAACCAGCCGGTCGGGCTCAGGAAGTCTACATGGATGCCGACG

# ^^^ this executed practially instantly. I had the answer before I had a chance to think anything after hitting run. My algorithm was so slow it took 2 minutes or so for the exact same result. On larger data sets that runtime difference would be absolutely insane. Ok. I guess a good lesson here is to just realize that when my problem involves manipulating a large amount of data, or possibly doing a large amount of computations, fundamentally efficinet strategies are quite important. 



######----- Pathfinder's solution -----#######################################
# 

# An alternative Solution that make my work look stupidly conceived: 
# from Pathfinder: 

# what is confusing here is that substrings must be sought automatically here (line 94)... some underlying Python capability I didn't know about
def lcsm(dnas):
    min_dna = min(dnas, key=len)

    for length in range(len(min_dna), 0, -1):
        for start in range(0, len(min_dna)-length+1):
            substrng = min_dna[start:start+length]
            found = True
            for dna in dnas:
                if substrng not in dna: 
                    found = False
                    break
                if found:          
                    return substrng
    return ''

lcss = lcsm(prepSeqs("C:\\Users\\Tanner_N\\Downloads\\rosalind_lcsm (1).txt"))
print(lcss)  # ok the first entire string itself of the data in was returned... not a substring at all.. makes me wonder if my data in was wrong to the function. 
#  It looks like this function literally does the same thing as my code.. however, it is returning the first substring that matches a SINGLE other string.. not checking for a match against all... wonder how this guy completed the problem, but otherwise I can see that his code has some better structure than my own overly complex bullshit. 
#  GTGATCTATGAACTGTTAGGTTACATTACCAGACTATGACTGTCAGCATAGACGGATGCCGCCTTTCTCGGTTAGGCGGCCCTGTCGTTCGCTACAAAGAAGTTGACACGCTAAAATTGTATATGGCGTCCGAATCTGACGGACAGTGCGGCATCTATGATACACCCTACCTTACGGCCTACGGTAGCGTCTCCGCCGTCCAGATGTCCCATTTGCCCGCACGAAATATTCTCGTTCCCAACAACGTTATACATAAAACGAAGCTATCGCCTAATACCCCAGTATCAACTGTCTCATGACACATGAATGCCAAAATGATCTATGCCCGTCACACTTATGCCACATTACGATGAAGATGTATCAAAGCCTTGTGACGCTATAGTCCTATAGGACGATTACCCAACTGGAGAGCGATGTCTCTGCTCTTTTTACGGTCCGAGGGAGTACACTTTGTCGATTAGTGCATGCGCGGAGGAACCAGCCGGTCGGGCTCAGGAAGTCTACATGGATGCCGACGGGAGCAACCCCGGCCGGGGAATAAGGGAAGTGAAGTTAAGCCGAAAACCTTATAAATCCCTTTTTTCGTAGCGGCGAAGAGTGTTCGATCAGATTCAGTTCAGCTCGGATTGAAGCTGATTGTTCGTTAAGGGAACACCTCTCATCCTGTGTATCCTAGCGTCTTTGTAACAATAAAGGGTCCCCTGCGTAAGGAAAGACTACAGGTGGCTCTCAAGTACTGCGAGTCCTACTGAGCGCTCCATATGACGTGCAGAATAATTCAAGTCGGATAAGGTTTGTCGGTCGTTCTCGCATTGGCCGTACTAGTCCGGACGTTCGTGACGTACGATGGTTATCGAAGTACAATACGAATAGCCAGACGCGCGCTACTGCTCCAACGAGCACGCCAGCTGTCCGTAAAGCAGATAAGTACACTAGTGACGATCCACGCCCCCGACTAATTATTGAATCACATATGACAGGAGTTGAACGAATTTTGGTA

for i in range(100, 0, -1): # Know how to do this whenever you want.. for loops can count however you need them to. 
    print(i)