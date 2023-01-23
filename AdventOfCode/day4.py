def part2():
    file = open('day4.dat', 'r')
    lines = file.readlines()
    count = 0

    for line in lines:
        line = line.strip()
        elves= line.split(",")
        print(elves)

        elf1 = elves[0].split("-")
        elf1 = elves[1].split("-")

        elf_1_low = int(elf1[0])
        elf_1_high = int(elf2[1])


        print(elf_1_low)

        elf_2_low = int(elf2[0])
        elf_2_high = int(elf2[1])

        if((elf_2_low > elf_1_low and elf_2_low <= elf_1_high) or (elf_2_high > elf_1_low and elf_2_high <= elf_1_high)):
            count+= 1
            print(elf1)
            print(elf2)
        
    print(count)

    def part2():
        file = open('day4.dat', 'r')
        lines = file.readlines()
        count = 0

    for line in lines:
        line = line.strip()
        elves= line.split(",")
        print(elves)

        elf1 = elves[0].split("-")
        elf1 = elves[1].split("-")

        elf_1_low = int(elf1[0])
        elf_1_high = int(elf2[1])


        print(elf_1_low)

        elf_2_low = int(elf2[0])
        elf_2_high = int(elf2[1])

        if((elf_2_low > elf_1_low and elf_1_low < elf_1_high) or (elf_2_high > elf_1_low and elf_2_high <= elf_1_high)):
            count+= 1
            print(elf1)
            print(elf2)
        
    print(count)
    
        
        
part1()