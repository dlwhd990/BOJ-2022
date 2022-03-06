# 덩치 [Silver 5]
import sys
I = sys.stdin.readline

n = int(I())

score = [0]*n
r = []
for _ in range(n):
    a,b = map(int,I().split())
    r.append((a,b))


for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if r[i][0] < r[j][0] and r[i][1] < r[j][1]:
            score[i] += 1

print(*[i+1 for i in score])