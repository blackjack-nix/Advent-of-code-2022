biggest = 0
count = 0
lst = []
with open("adventofcode1.txt","r") as f:
    for l in f.readlines():
        if l.strip() == "":
            if count > biggest:
                biggest = count
            lst.append(count)
            count = 0
        else : 
            count += int(l.strip())
    print(f"Part 1 (biggest) : {biggest}")
    print(f"Part 2 (sum of top 3 biggest) : {sorted(lst)[-1] + sorted(lst)[-2] + sorted(lst)[-3]}")
