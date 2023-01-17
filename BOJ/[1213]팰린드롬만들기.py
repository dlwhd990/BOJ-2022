# 팰린드롬 만들기 [Silver 3]
import sys
I = sys.stdin.readline

a = I().rstrip()
tmp = ''

d = dict()
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1


t = sorted(list(d.keys()))

for i in t:
    tmp += (i*(d[i]//2))
    d[i] -= (d[i]//2)*2

vList = list(d.values())
if vList.count(0) == len(vList):
    print(tmp+tmp[::-1])

elif vList.count(1) == 1 and vList.count(0) == len(vList)-1:
    for i in d.keys():
        if d[i] == 1:
            print(tmp+i+tmp[::-1])
            break

else:
    print("I'm Sorry Hansoo")
