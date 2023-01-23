def part1():
    file = open('day2-2020.dat', 'r')
    lines = file.readlines()
    answer = 0
    invalid = 0
    valid = 0

    for line in lines:
        count = 0
        line1 = line.strip() 
        password = line1.split(": ",1)[1]
        policy = line1.partition(" ")[0]
        policyArr = policy.split("-")
        policy1 = int(policyArr[0])
        policy2 = int(policyArr[1])
        letterNF = line1.split(" ",1)[1]
        letter = letterNF.partition(":")[0]
    
        print(password)
        print(policy1)
        print(policy2)
        print(letter)
    
        for l in password:
            
            if (letter == l):

                count+= 1
                
        if(count >= policy1 and count <= policy2):
            valid += 1
    
    print(valid)



def part2():
    file = open('day2-2020.dat', 'r')
    lines = file.readlines()
    answer = 0
    invalid = 0
    valid = 0

    for line in lines:
        count = 0
        line1 = line.strip() 
        password = line1.split(": ",1)[1]
        policy = line1.partition(" ")[0]
        policyArr = policy.split("-")
        policy1 = int(policyArr[0])
        policy2 = int(policyArr[1])
        letterNF = line1.split(" ",1)[1]
        letter = letterNF.partition(":")[0]
    
        print(password)
        print(policy1)
        print(policy2)
        print(letter)
    
        for l in password:
            
            if (letter == l):

                count+= 1
                
        if(count >= policy1 and count <= policy2):
            valid += 1
    
    print(valid)
       
        


part1()