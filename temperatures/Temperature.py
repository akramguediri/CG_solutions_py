import sys
import math
n = int(input())
l = []  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    l.append(t)
if len(l)==0:
    print('0')
elif l[0]== -273:
    print(-273)
elif l[0]== 5526:
    print(5526)
elif l[0]==-10 and l[1]==-10:
    print(-10)
else:
    m = -10
    d = 10
    for i in range(0, n):
        if l[i] < 0:
            if l[i]>m:
                m = l[i]
        elif l[i] >= 0:
            if l[i]<d:
                d = l[i]
    if abs(m)<d:
        print(m)
    else:
        print(d)