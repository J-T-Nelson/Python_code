
# Sharno's solution: Oct. 8, 2013
fileIn = open("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc (1).txt", 'r')
s = fileIn.read()

genes = s.split(">")[1:]
gc = []

for gene in genes:
    a = gene.count("C") + gene.count("G")
    b = gene.count("C") + gene.count("G") + gene.count("A") + gene.count("T")
    gc.append(float(a)*100/b)

print(genes[gc.index(max(gc))][:13])
print(max(gc))

#I sort of wounder if calling count 4 times was better than just removing the Rosalind_9999 tag and then removing all '\n' with .replace() ... I suppose it really doesn't matter, either way this is a very elegant solution comapred to mine once again. My means of parsing the text was very overdesigned and clearly showed just how inexperienced I really am. 

# some useful notes from other commenters on this solution 
########################################################
# Very efficient solution IF

# 1. We know the (constant)length of the FASTA name
# 2. the FASTA name does not have a 'G' 'A' 'T' 'C'.

# Works well here because the two rules hold true. But the code would fail for a general-case FASDA format.
# As a matter of principle, it is necessary to solve for the general case, on Rosalind?
# In real life, I'd say, yes, absolutely necessary. But here?
########################################################



########################################################
# One thing I notice for a lot of nucleotide counting is people tend to count the individual letters, while this works for small cases, this would take a very long time for a large sequence and isn't very efficient because you end up looping through the string 6 times in this example.

# The best strategy to count nucleotides and save compute power is to cache them in a dictionary in python with something like this where it loops through the string once:

# steve-barnard solution (it may be a partial solution, but still insightful for the handling of DNA data)

def gc_content(seq):
    nuc = {
    'A': 0,
    'T': 0,
    'G': 0,
    'C':0,
    'length': 0,
    'GC Content': 0}

    for i in seq:
        nuc[i] += 1

    nuc['length'] = len(seq)
    nuc['GC Content'] = ((nuc['G'] + nuc['C']) / nuc['length'] ) * 100

    return (nuc['GC Content'], nuc)

