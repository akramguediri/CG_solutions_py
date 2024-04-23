s=''
t=[]
r=''
m = input()
for i in m:
    s+=bin(ord(i)).replace('0b','').zfill(7)
s=s.replace('01','0 1')
s=s.replace('10','1 0')
t=s.split()
for i in t:
    if '1' in i:
        r+='0'+' '+'0'*len(i)+' '
    else:r+='00'+' '+'0'*len(i)+' '
print(r[0:len(r)-1])