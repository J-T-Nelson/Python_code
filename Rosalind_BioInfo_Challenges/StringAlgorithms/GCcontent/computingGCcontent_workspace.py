# In practice, the GC-content of most eukaryotic genomes hovers around 50%. However, because genomes are so long, we may be able to distinguish species based on very small discrepancies in GC-content; furthermore, most prokaryotes have a GC-content significantly higher than 50%, so that GC-content can be used to quickly differentiate many prokaryotes and eukaryotes by using relatively small DNA samples.

# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated

# DEF: Absolute Error - "a measure of how close a computed value is to a correct value" 
# DEF: Numerical Analysis - "The mathematical study of computational approximation"


# for this challenge the text of the strings will be much larger than before, thus I should start importing files for the functions instead of dropping the strings in directly. 

# pseudocode: 
    # create dictionary 
    # create scanner
    # while( lines still in file)
    #     store the name of the entry 
    #     scan for >* on a line, then scan in the rest of the text up until the next > is reached
    #     store those scanned lines as a string, 
    #     count the num of C and G by replacing A and T with nothing, (store this inside a new variable)
    #     make dictionary entry using name of entry and length(AT removed from string) / length(original string)

    # getIndexOfHighestPercent = which(max(dictionary values))
    # returnString = dictionary(highestStringKey) +"\n" + dictionary(highestStringValue)
    # return(returnString)

from fileinput import filename
import timeit

s1 = "TGGGAACCTGCGGGCAGTAGGTGGAAT"
print("Printing s1: " + s1)
print("Printing s1 with A and T removed: " +s1.replace('A', '').replace('T',''))



fileIn = open("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\GCcontTest.txt", 'r')
#fileCont = fileIn.read() # HERE IS OUR ISSUE. We must be moving the pointer all the way through our file by reading it like this. YES. this is the problem. good to know. .read() will move the pointer to the very end of the file, thus iterating through it is impossible 
testDict = {}
for line in fileIn:

    #print(line, end="")
    #print("fileIn.tell() contents: ")
    #print(fileIn.tell()) # OSError: telling position disabled by next() call ... ok so somehow calling next() is affecting .tell()

    if '>' in line:
        dKey = line
        contrl = next(fileIn)
        dString = ''
        try:
            while '>' not in contrl and fileIn: 
                dString = dString + contrl
                contrl = next(fileIn) # THIS LINE is causing an error, which must be caught called 'StopIteration' .. read on how to error catch and upon catching it, exit the while loop. The behavior of the for loop is otherwise working really well! good job me. You are close to finishing this difficult challenge I think.
        except:
            dString = dString.replace('\n' , '')
            gcString = dString.replace('A', '').replace('T', '').replace('\n', '')
            testDict[dKey] = (len(gcString)/len(dString))




fileIn2 = open("D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\GCcontTest.txt", 'rb')
print("contents of PEEK: ", end='')
print(fileIn2.peek()) #'>Rosalind_6404\r\nCCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC\r\nTCCCACTAATAATTCTGAGG\r\n>Rosalind_5959\r\nCCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT\r\nATATCCATTTGTCAGCAGACACGC\r\n>Rosalind_0808\r\nCCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC\r\nTGGGAACCTGCGGGCAGTAGGTGGAAT'
print("contents of PEEK with utf-8 decoding: " + fileIn2.peek().decode('utf-8')) # alright so peek is an option.. but for some reason its pretty limited in python. Not the same as java. Therefore, we must instead use seek() 
#print(testDict)
# print(fileCont)
# fileIn.close()


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


testFile = "D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\GCcontTest.txt"

testDict = GCcontDict(testFile)
print(testDict)
getLargestValDict(testDict)

#print(highestGCcontent(testFile))

challengeFile = "D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc.txt"
print(GCcontDict(challengeFile))
print(highestGCcontent(challengeFile))

challengeFile2 = "D:\\Programming\\Python_code\\Rosalind_BioInfo_Challenges\\StringAlgorithms\\rosalind_gc (1).txt"
print(GCcontDict(challengeFile2))
print(highestGCcontent(challengeFile2))


fileIn.close()
fileIn2.close()