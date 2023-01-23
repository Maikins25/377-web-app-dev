def part1(): 
    file = open('day3.dat', 'r')
    lines = file.readlines()
    total = 0

    for line in lines:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        second_half = second_half[:-2]

        for letter in first_half:
            if letter in second_half:
                total = getPriority(letter) + total

    print(total)

def getPriority(letter):
    priority = ord(letter)
    if(priority > 96):
        priority  = priority -  96
    else:
        priority = priority - 38 
        
part1()