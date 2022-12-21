
#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# so we need a formula which calculates the probability that an offspring carries one or more dominant alleles 

from xml import dom


def dominantAlleleProb(homoD, hetD, homoR):
    totalPop = homoD + hetD + homoR
        # accounting for prob of fully recessive baby completely by calculating each tree branch with this outcome (REFERENCE https://rosalind.info/problems/iprb/ for the tree )
    homoRhomoR = (homoR/totalPop) * ((homoR-1)/(totalPop-1)) 
    hetDhomoR =  (hetD/totalPop) * ((homoR)/(totalPop-1)) * (1/2)  
    homoRhetD = (homoR/totalPop) * ((hetD)/(totalPop-1)) * (1/2)
    hetDhetD = (hetD/totalPop) * ((hetD-1)/(totalPop-1)) * (1/4) # this multiplication factor of 1/4th may be incorrect... it may be 3/4ths. as possibly offspring for Aa x2 == AA, Aa, Aa, aa. 
        # prob(dominant Progeny) = 1 - (prob recessive progeny)
    return(1 - (homoRhomoR + hetDhomoR + homoRhetD + hetDhetD) )



print(dominantAlleleProb(2,2,2)) # correct for the toy example.. not sure how to test for other examples unless I manually calculated the whole dang tree

print(round(dominantAlleleProb(29,28,29), 5)) # SUCCESS ... this produced the correct answer. 

#  calculate prob of getting recessive 2 times... doesn't account for hetD ... its going to be prob of 1 homoR or 1 hetD/2 * 

# 1 homoR + 1 homoR after removing 1 from total ...

# if we use the tree diagram method I think we need to essentially calculate the actual tree... is there a simpler formula which works though? 


# so their number comes from 47/60, which implies that 13/60 is the probability of getting a recessive only baby. 



