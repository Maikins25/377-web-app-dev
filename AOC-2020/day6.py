
arrLetters = []

def part1():
    file = open('day6.dat', 'r')
    lines = file.readlines()
    arr = []
    arr2 = []
    gcount = 0
    
    for line in lines:
        if(line.strip() != ''):
            arr.append(line)
        else:
            arr.append(" ")
        
    #gets rid of the /n on all of the indexes of the array
    for i, line in enumerate(arr):
        arr[i] = line.rstrip('\n')

    arr2 = []
    string = ""
    for line in arr:
        if line != " ":
            string += line
        elif line == ' ':
            arr2.append(string)
            string = ''
    
    for item in arr2:
        arrLetters = [] 
        for letter in item:
   
            if(letter in arrLetters):
                gcount = gcount
                # print(arrLetters)
                # print(gcount)
            elif(letter not in arrLetters):
                
                arrLetters.append(letter)
                gcount += 1
                # print(arrLetters)
    print(gcount)








def part2():
    file = open('day6.dat', 'r')
    lines = file.readlines()
    arr = []
    arr2 = []
    gcount = 0
    for line in lines:
        if(line.strip() != ''):
            arr.append(line)
        else:
            arr.append(" ")
        
    #gets rid of the /n on all of the indexes of the array
    for i, line in enumerate(arr):
        arr[i] = line.rstrip('\n')

    print(arr)
    arrLetters = [] 
    for item in arr:
        for letter in item:
            arrLetters.append(letter)

        if(item != ' '):

            for letter in item:
                if(letter in arrLetters):
                    

                else:
                    arrLetters = []
                
                    
                    
                    
            
                    
        else:
            arrLetters = []
            
    print(gcount)

    

            
            

            



 
        
#go through arr and get every line in a single group and put it into an array, then use numpy to make an array of those arays and 
#iterate through each group to check if every person in the group answered each question that was answered by anyone in the group(use
# code from part 1 for that), then add to the final count for every quesrtion that was answered by an entire group.
    
    
    
   

            
        


        



part2()

#use on group list to check if the letters are unique in the group

 
