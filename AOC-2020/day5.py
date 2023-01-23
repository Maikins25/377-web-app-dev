seatIdArr = []

def part1():
    file = open('day5.dat', 'r')
    lines = file.readlines()
    rowList = []

    for line in lines:
        value = 2
        seatNum = line.strip()[7:]
        string = line.strip()[:7]
        
        seatNumArr = []
        
       
        for number in seatNum:
            
            if (number == 'R'):
                seatNumArr.append(0)
            else:
                seatNumArr.append(1)
            

        for letter in string:
            if (letter == 'F'):
                rowList.append(0)
            else:
                rowList.append(1)

        rNum = (getRow(rowList))
        cNum = (getCollumn(seatNumArr))
        
        seatId = (rNum * 8) + cNum
        seatIdArr.append(seatId)
        # print(seatId)
        rowList = []
    
    
    # print(seatIdArr)
    # print(getHighestId())
       



def getRow(list):
    allRows = []

    for i in range(0,128):
        allRows.append(i)

   
    rows = allRows[:len(allRows)//2]
    seatNum = allRows[len(allRows)//2:]
   
    for num in list:
        if(num == 0):
            allRows = allRows[:len(allRows)//2]
            
        else:
            allRows = allRows[len(allRows)//2:]
    rowNum = stupid(allRows)
    return rowNum
    


def getCollumn(list):
    seatNum = [0,1,2,3,4,5,6,7]
    seatNum2 = [0,1,2,3,4,5,6,7]
    

#splits the list of row numbers into halfs based on the number that is in the list
    for num in list:
        if(num == 1):
            seatNum = seatNum[:len(seatNum)//2]
            
        else:
            seatNum = seatNum[len(seatNum)//2:]
    collumnNum = stupid(seatNum)
    return collumnNum
    



def stupid(list):
    for num in list:
        return num

    
def getHighestId():
    cur = 0
    for num in seatIdArr:
        if(num > cur):
            cur = num
    

def part2():
    # print(seatIdArr)
    answer = 0
    seatIdArr.sort()
    print(seatIdArr)
    
    for number in seatIdArr:
        if(number + 1 not in seatIdArr):
            answer = number + 1
            break
        
    print(answer)

   

part1()

part2()

