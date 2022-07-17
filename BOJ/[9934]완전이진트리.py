#https://www.acmicpc.net/problem/9934
#완전 이진 트리 [Silver 1]
import sys
I = sys.stdin.readline

k = int(I())
a = list(map(int,I().split()))

visited = [0]*(len(a)+1)
r = []
result = [0]*(len(a)+1)

idx = 2**(k-1)

while idx < (2**k)-1:
    if visited[idx] == 0:
        if idx*2 > len(visited)-1:
            r.append(idx)
            visited[idx] = 1
            idx //= 2

        elif visited[idx*2] == 0:
            idx = idx*2

        elif visited[idx*2] == 1:
            r.append(idx)
            visited[idx] = 1

        elif visited[idx*2+1] == 0:
            idx = idx*2+1


    else:
        if idx*2+1 > len(visited)-1:
            idx //= 2

        elif visited[idx*2+1] == 1:
            idx //= 2

        else:
            idx = idx*2+1

r.append(2**k-1)

for i in range(len(a)):
    result[r[i]] = a[i]

for i in range(1,k+1):
    print(*result[2**(i-1):2**i])