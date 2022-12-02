count = 0
with open("adventofcode2.txt","r") as f:
    for l in f.readlines():
        l = l.split()
        if l[0] == 'A':
            if l[1] == 'X':count += (3 + 0)
            if l[1] == 'Y':count += (1 + 3)
            if l[1] == 'Z':count += (2 + 6)
        elif l[0] == 'B':
            if l[1] == 'X':count += (1 + 0)
            if l[1] == 'Y':count += (2 + 3)
            if l[1] == 'Z':count += (3 + 6)
        elif l[0] == 'C':
            if l[1] == 'X':count += (2 + 0)
            if l[1] == 'Y':count += (3 + 3)
            if l[1] == 'Z':count += (1 + 6)
    print(count)
