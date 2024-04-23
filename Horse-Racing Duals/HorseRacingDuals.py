import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
t=[]
t2=[]
j=0
n = int(input())
for i in range(n):
    pi = int(input())
    t.append(pi)
t.sort()
while j< len(t)-1:
    t2.append(t[j+1]-t[j])
    j+=1
t2.sort()
print(t2[0])
