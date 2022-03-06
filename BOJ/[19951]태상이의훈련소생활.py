# 태상이의 훈련소 생활 [Gold 5]
import sys
I = sys.stdin.readline

n,m = map(int,I().split())
ground = list(map(int,I().split()))

start = [[]for _ in range(n)]
end = [[]for _ in range(n)]

for _ in range(m):
    s,e,h = map(int,I().split())
    start[s-1].append(h)
    end[e-1].append(h)

state = 0
for i in range(n):
    if len(start[i]) > 0:
        state += sum(start[i])

    ground[i] += state

    if len(end[i]) > 0:
        state -= sum(end[i])

print(*ground)