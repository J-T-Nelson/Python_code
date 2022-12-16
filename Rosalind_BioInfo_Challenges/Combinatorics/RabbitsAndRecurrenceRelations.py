
# DEF: recurrence relation - "An equation defining terms of a sequence with respect to previous terms"

def rabbitReproduction(months, offspringPairs):
    numReproducers = 2 
    if months == 0 or months == 1 or months == 2:
        return(numReproducers)

    numOffspring = 0
    temp = 0 #prev gen offspring which = maturing offspring. 
    for i in range(months - 2):
        temp = numOffspring
        numOffspring = numReproducers * offspringPairs
        numReproducers = numReproducers + temp
    return(int((numReproducers+numOffspring)/2))

print(rabbitReproduction(5, 3))
print(rabbitReproduction(3, 3))
print(rabbitReproduction(4, 3))

print(rabbitReproduction(1, 1))
print(rabbitReproduction(2, 1))
print(rabbitReproduction(3, 1))
print(rabbitReproduction(4, 1))
print(rabbitReproduction(5, 1))
print(rabbitReproduction(6, 1))
print(rabbitReproduction(7, 1))

print(rabbitReproduction(33, 3)/2)
# # THINK THIS PROBLEM IS BUGGED... HERE IS MY CRITQUE I AM REPORTING TO ROSALIND... though I think the site is deprecated. 

# I believe this problems sample output must be wrong. 

# Reading this prompt it can be understood that we MUST start with 2 rabbits, and further that each pair of rabbits produces k PAIRS of rabbits. "Pair" implies that the smallest unit is an even number (2). This is to say, that each time new rabbits are generated, an even number is generated. And since we also start with an even number of rabbits. Having an odd sum of rabbits at any generation is impossible. Thus 19 cannot possibly be a valid answer to prompt, as it is an odd number. 

# ok.. the issue is they want you to return the number of rabbit pairs... lol .... kind of annoying they would do that.. 

def fibSeq(n):
    # n = nth # of fibonacci sequence
    if n == 0:
        return(0)
    if n == 1 or n == 2:
        return(1)
    
    term_1 = 1
    term_2 = 1
    temp = 0
    for i in range(n-2):
        temp = term_1 + term_2
        term_1 = term_2
        term_2 = temp
    return(term_2)
    
for i in range(20):
    print(fibSeq(i)) # NICE. our sequence works... it may not be the most beautiful, but it is functional. 





