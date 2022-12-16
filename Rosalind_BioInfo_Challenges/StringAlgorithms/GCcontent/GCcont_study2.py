import timeit
# from Rosalind_BioInfo_Challenges.StringAlgorithms.computingGCcontent import highestGCcontent

# from TestCode.benchmarkingPractice import bestTime

# THIS IS serg5978's solution from jan. 31, 2016. 


def GCcountStudy2():
    f = open('D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc (1).txt', 'r' )
    data = f.read()

    lst = data.split('>')
    print(lst)
    res = {}
    for i in lst:
        if len(i) > 0:
            temp = ''.join(i[13:].split())
            perc = ((temp.count('C') + temp.count('G'))/len(temp))*100
            res[perc] = i[:13]

    print(res[max(res)])
    print(max(res))

    f.close()

# EXAMPLE: 
setup = "def make_list(): return [_ for _ in range(10)]"
#####


def bestTime(t, digits = 4):
    return (round(min(t), digits))

statement = '''
f = open("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc (1).txt", 'r' )
data = f.read()

lst = data.split('>')
print(lst)
res = {}
for i in lst:
    if len(i) > 0:
        temp = ''.join(i[13:].split())
        perc = ((temp.count('C') + temp.count('G'))/len(temp))*100
        res[perc] = i[:13]

print(res[max(res)])
print(max(res))

f.close()
'''
#t1 = timeit.repeat(stmt=statement) # getting a challenging error with this. chatGPT isn't able to help either. 
# ERROR ^^ : OSError: [Errno 22] Invalid argument: 'D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\rosalind_gc (1).txt'
#t2 = timeit.repeat(highestGCcontent('D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc (1).txt'))
#print(bestTime(t1))
#print(bestTime(t2)) # need to know how to import modules / add them to the search path for python compiler(?) such that I can call my own functions from separate files. 
path = "D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc (1).txt"
print(len(path))

# doing a function wrapped benchmark instead of a snippet API benchmark 

t3 = timeit.repeat(GCcountStudy2)
print(min(round(t3, 4)))

