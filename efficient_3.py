import sys
"""
resource module does not work on windows environment
remove the comment if running this program in Unix
"""
# from resource import *
import time
import psutil

"""Set value of DELTA to 30"""
GAP_PENALTY = 30
"""
Set alpha value for each character pair followed the requirement:
    A   C   G   T
A   0  110  48  94
C  110  0   118  48
G  48  118  0   110
T  94  48   110  0
"""
MISMATCH_PENALTY = {
    "A" : {
        "A" : 0,
        "C" : 110,
        "G" : 48,
        "T" : 94,
    },
    "C" : {
        "A" : 110,
        "C" : 0,
        "G" : 118,
        "T" : 48
    },
    "G" : {
        "A" : 48,
        "C" : 118,
        "G" : 0,
        "T" : 110,
    },
    "T" : {
        "A" : 94,
        "C" : 48,
        "G" : 110,
        "T" : 0
    }
}

list1 = []
list2 = []

def readFile(filePath):
    with open(filePath,'r') as file:
        fileData = file.readlines()
    string1 = fileData[0].strip()
    print(string1, "\n")
    current = 1
    for data in fileData[1:]:
        if data.strip().isdigit():
            data = int(data.strip())
            list1.append(data)
            current += 1
        else:
            break
    
    string2 = fileData[current].strip()
    print(string2, "\n")
    current += 1
    for data in fileData[current:]:
        if data.strip().isdigit():
            data = int(data.strip())
            list2.append(data)
            current += 1
        else:
            break
    return string1, string2

def createSequence(str, ls):
    strList = list(str)
    temp = ''.join(strList)
    print(strList)
    for i in range(len(ls)):
        strList.insert(ls[i] + 1, temp)
        temp = ''.join(strList)
    return temp
    
"""
Basic way to create 2D DP array
TODO: Modify to Efficient version
"""
def setBoard(sequence1, sequence2):
    length = len(sequence1) + 1
    width = len(sequence2) + 1
    
    dp = [[0 for i in range(length)] for j in range(width)]

    for a in range(1, width):
        dp[0][a] = dp[0][a-1] + GAP_PENALTY
    
    for b in range(1, length):
        dp[b][0] = dp[b-1][0] + GAP_PENALTY
    
    for row in range(1, length):
        for col in range(1, width):
            if sequence1[row - 1] is sequence2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = min(dp[row - 1][col - 1] + MISMATCH_PENALTY[sequence1[row]][sequence2[col]],
                    dp[row - 1][col] + GAP_PENALTY,
                    dp[row][col - 1] + GAP_PENALTY)

    return dp

def getAlignment(dp):
    return NotImplemented

def writeFile(outputPath,penaltyCost, alignment1, alignment2, timeUsed, memoryUsed):
    with open(outputPath, 'w') as file:
        file.write(penaltyCost,"\n")
        file.write(alignment1,"\n")
        file.write(alignment2,"\n")
        file.write(timeUsed,"\n")
        file.write(memoryUsed, "\n")
    


def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

def time_wrapper():
    start_time = time.time()
    """
    TODO: call algorithm here
    """
    call_algorithm()
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    return time_taken





if __name__ == '__main__':
    intputPath = sys.argv[1]
    # outputPath = sys.argv[2]

    inputStr1, inputStr2 = readFile(intputPath)
    # memoryBefore = process_memory()

    """
    TODO: In timeWrapper(), generate the 2d DP array,
    based on the dp array, generate the alignment sequence
    after the alignments generated, calculate the penalty cost
    """
    # timeUsed = timeWrapper()
    

    # memoryAfter = process_memory()

    # memoryUsed = memoryAfter - memoryBefore
    # writeFile(outputPath, penaltyCost, alignment1, alignment2, timeUsed, memoryUsed)