
total = 0
f0 = 1
f1 = 2
fnext = f0 + f1


while f1 < 4000000:
    if f1 % 2 == 0:
        total += f1

    f0 = f1
    f1 = fnext
    fnext = f0 + f1

print(total)