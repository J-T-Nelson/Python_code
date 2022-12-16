
#LudditeCyborg's solution. 
# this one is pretty clever, using string manipulation in a pretty unexpected way that makes a lot of sense. 
# the programmer takes advantage of the symbols which naturally delinate lines or order to create arrays which can be regularly handled given the regular form of the code. 


dnafile = open('rosalind_gc.txt', 'r')
raw = dnafile.read()
d = {}
for seqblock in raw.split(">")[1:]:
    parts = seqblock.split("\n")
    fasta = parts[0]
    seq = ''.join(parts[1:])
    gc = 100 * ( seq.count("G") + seq.count("C") ) / float(len(seq))
    d[gc] = fasta
print(d[max(d)], max(d))
