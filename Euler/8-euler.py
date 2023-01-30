

nums = []


def part1():
    file = open('8-euler.dat', 'r')
    lines = file.readlines()
    
    count = 0
    


    while count <= 13:      
        for line in lines:
            for num in line.strip():
                
                nums.append(int(num))
                count += 1
        
        print(nums)
    
    tail = 0
    head = 13
    maxProd = 0

    for i in range(0, len(nums) - 13):
        curProd = 1

        subArray = nums[tail:head]
        for num in subArray:
            curProd *= num


        if curProd > maxProd:
            maxProd = curProd
        tail += 1
        head += 1
    print(maxProd)

part1()
