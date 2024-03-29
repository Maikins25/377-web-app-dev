moves = []

def getCode():
    code = ''

    for stack in stacks:
        code = code + stack.pop()

    return code


def initializeStacks():
    # Snippet:
    # return [ ['Z', 'N'], ['M', 'C', 'D'], ['P'] ]

    # Full:
    return [ ['J', 'H', 'G', 'M', 'Z','N','T','F'],
             ['V', 'W', 'J'],
             ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
             ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
             ['F', 'W', 'S','M','P','R','G'],
             ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],
             ['D', 'H', 'G', 'M', 'R'],
             ['H', 'N', 'M', 'V', 'Z', 'D'],
             ['G', 'N', 'F', 'H'] ]


def loadData():
    global moves

    file = open('day5.dat', 'r')
    lines = file.readlines()

    instruction = False
    for line in lines:
        line = line.strip()
        if (instruction):
            pieces = line.split()
            moveCount = int(pieces[1])
            moveFrom = int(pieces[3]) - 1
            moveTo = int(pieces[5]) - 1
            moves.append([moveCount, moveFrom, moveTo])
        elif (line == ''):
            instruction = True


def part1():
    count = 0

    for move in moves:
        # print(move)
        moveCount = move[0]
        moveFrom = move[1]
        moveTo = move[2]

        for i in range(moveCount):
            item = stacks[moveFrom].pop()
            stacks[moveTo].append(item)

        count = count + 1
        # showStacks(count)

    print("Part 1: " + getCode())


def part2():
    count = 0

    for move in moves:
        # print(move)
        moveCount = move[0]
        moveFrom = move[1]
        moveTo = move[2]

        for i in range(moveCount):
            item = stacks[:3]
            stacks[moveTo].append(item)

        count = count + 1
        # showStacks(count)

    print("Part 1: " + getCode())




