# 나이순 정렬 [Silver 5]
import sys
I = sys.stdin.readline
r = []
n = int(I())
for i in range(n):
    a,b = I().rstrip().split()
    r.append((int(a),i,b))

r.sort(key=lambda x:(x[0],x[1]))

for i in r:
    print(i[0],i[2])