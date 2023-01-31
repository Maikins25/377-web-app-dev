
def part1():
    file = open('13-euler.dat', 'r')
    lines = file.readlines()

    total = 0
    for line in lines:
        total += int(line.strip())

    print(total)

    total = str(total)

    answer = []
    count = 0
    
    for num in total:
        answer.append(num)
        count += 1
        if count >= 10:
            break
    print(answer)
        

part1()