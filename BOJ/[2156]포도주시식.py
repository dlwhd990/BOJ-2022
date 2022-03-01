import sys
I = sys.stdin.readline

n = int(I())
podo = []
for _ in range(n):
    podo.append(int(I()))

d = [0]*n

if n == 1:
    print(podo[0])

elif n == 2:
    print(podo[0]+podo[1])


else:
    d[0] = podo[0]
    d[1] = podo[0]+podo[1]
    d[2] = max(podo[0]+podo[2],podo[1]+podo[2],podo[0]+podo[1])

    for i in range(3,n):
        d[i] = max(d[i-3]+podo[i-1]+podo[i],d[i-2]+podo[i])
        d[i] = max(d[i],d[i-1])

    print(max(d))