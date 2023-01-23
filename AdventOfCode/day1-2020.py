def part1():
    file = open('day1-2020.dat', 'r')
    lines = file.readlines()
    currentNum = 0
    answer = 0

    for line in lines:
        currentNum = int(line.strip())
        for a in lines:
            if (int(a.strip()) + currentNum == 2020):
                answer = int(a.strip()) * currentNum
    
    print(answer)

    

def part2():
    file = open('day1-2020.dat', 'r')
    lines = file.readlines()
    currentNum = 0
    answer = 0

    for line in lines:
        currentNum = int(line.strip())
        for a in lines:
            for b in lines:
                if ( int(a.strip()) + int(b.strip()) + currentNum == 2020):
                    answer = int(a.strip()) * int(b.strip()) * currentNum
    
    print(answer)
                
part2()



