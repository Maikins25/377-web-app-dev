def part1():
    file = open('day6-2020.dat', 'r')
    line = file.readline().strip()
    counter = 0

    for i in range(len(line) - 13):
        chunk = line[i:i+14]
        counter = counter + 1 


        Chunkset = set()

        for c in chunk:
            Chunkset.add(c)
            
            

        if(len(Chunkset) == 14):
             print(counter + 13)
             break
                      
      

part1()
