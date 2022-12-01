count, lst, l = 0, [], open("adventofcode1.txt","r")
for l in l.readlines():
    if l.strip() == "":
        lst.append(count)
        count = 0
    else : count += int(l.strip())
print(f"Part 1 (biggest) : {sorted(lst)[-1]}\nPart 2 (sum of top 3 biggest) : {sum(sorted(lst, reverse=True)[:3])}")
