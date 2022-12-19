#https://www.acmicpc.net/problem/20055
#컨베이어 벨트 위의 로봇 [Gold 5]
import sys
from collections import deque
I = sys.stdin.readline

n,k = map(int,I().split())
a = list(map(int,I().split()))

result = 1
top = deque()
bottom = deque()
robots = deque()

for i in range(n):
    top.append(a[i])
    bottom.append(a[-1-i])
    robots.append(0)

while True:
    cnt = 0
    bottom.append(top.pop())
    top.appendleft(bottom.popleft())
    robots.pop()
    robots.appendleft(0)
    if robots[-1] == 1:
        robots[-1] = 0

    for i in range(n-2,0,-1):
        if robots[i] == 1 and robots[i+1] == 0 and top[i+1] > 0:
            robots[i+1] = robots[i]
            robots[i] = 0
            top[i+1] -= 1

    if top[0] > 0:
        robots[0] = 1
        top[0] -= 1


    for i in range(n):
        if top[i] <= 0:
            cnt += 1
        if bottom[i] <= 0:
            cnt += 1

    if cnt >= k:
        print(result)
        break

    result += 1