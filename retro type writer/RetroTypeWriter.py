t = input().split()
for i in t:
    n = 0
    s = ""
    if i[0].isnumeric():
        if i[1].isnumeric() and len(i)>2:
            n = int(i[:2])
            s = i[2:]
        else:
            n = int(i[0])
            s = i[1:]
    if i == "nl":s = print()
    elif s == "sp": s = " "
    elif s == "bS": s = "\\"
    elif s == "sQ": s = "'"
    print(str(s)*n, end='')
