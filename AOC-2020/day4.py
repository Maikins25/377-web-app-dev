import re 
passports = []
requirements = ['byr',
                'iyr',
                'eyr',
                'hgt',
                'hcl',
                'ecl',
                'pid']

def loadData(dataFile):
    passport = {}

    file = open(dataFile, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line == '':
            passports.append(passport)
            passport = {}
        else:
            for element in line.split():
                k, v = element.split(':')
                passport[k] = v

    # Add the final passport to solve the fencepost problem
    passports.append(passport)


def part1():
    count= 0
    for passport in passports:
        if all(requirement in passport.keys() for requirement in requirements):
            count += 1

    print('Part 1: ' + str(count))


def part2():
    
    count= 0
    for passport in passports:
        # print(passport, "\n")
        if all(requirement in passport.keys() for requirement in requirements):    
            byr = int(passport["byr"])
            #Validate the birth year
            if byr < 1920 or byr > 2002:
                continue

          
            iyr = int(passport['iyr'])
            if iyr < 2010 or iyr > 2020:
                continue

            eyr = int(passport['eyr'])
            if eyr < 2020 or eyr > 2030:
                continue
            
            units = passport["hgt"][-2:]
            if units == 'in':
                value = int(passport["hgt"][:-2])

                if value < 59 or value > 76:
                    continue   
            elif units =='cm':
                value = int(passport["hgt"][:-2])
                if value < 150 or value > 193:
                    continue
            else:
                continue

            hcl = passport['hcl']
            if re.search (r'^#[0-9a-f]{6}$', hcl ) is None:
                continue

            print('here 3')

            ecl = passport['ecl']
            if ecl not in ['amb', 'blu', 'brn','gry','grn', 'hzl', 'oth' ]:
                continue
            
            print('here 4')

            pid = passport['pid']
            if re.search (r'^[0-9]{9}$', pid ) is None:
                continue


            print("here end")


            count += 1


    print('Part 2: ' + str(count))


loadData('day4-2020.dat')
part2()