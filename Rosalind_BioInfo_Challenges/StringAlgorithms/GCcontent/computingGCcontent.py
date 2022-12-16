import timeit

def GCcontDict(filePath):
    # reads a file with DNA data string and returns the GC-nucleotides/total-nucleotides ratio along with the label of the string with that value
    fileIn = open(filePath, 'r')
    Dict = {}
    seekPos = 0

    for line in fileIn:
        seekPos += len(line)
        if '>' in line:
            dKey = line.replace('\n', '').replace('>', '')
            contrl = next(fileIn)
            seekPos += len(contrl)
            dString = ''
            
            try:
                while '>' not in contrl: 
                    dString = dString + contrl
                    #prevPos = fileIn.tell() # this causes the OSError: telling position disabled by next() call bug which is caught by my except statement
                    contrl = next(fileIn)
                    seekPos += len(contrl) 
                    if '>' in contrl:
                        fileIn.seek(seekPos)

            except StopIteration: # catching StopIteration error that occurs when fileIn is empty within while loop 
                pass
            
            dString = dString.replace('\n' , '')
            gcString = dString.replace('A', '').replace('T', '').replace('\n', '')
            Dict[dKey] = ( (len(gcString)/len(dString))*100 )
    fileIn.close()
    return(Dict)

def getLargestValDict(Dictionary):
    largest = 0
    key = ''
    for item in Dictionary:
        dictVal = Dictionary.get(item)
        if dictVal > largest:
            largest = dictVal 
            key = item
    return key + "\n" + str(largest)
        
def highestGCcontent(filePath):
    return getLargestValDict(GCcontDict(filePath))

print(highestGCcontent("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc (1).txt"))

t1 = timeit.repeat("highestGCcontent('D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc (1).txt')")