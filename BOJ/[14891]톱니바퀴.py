# 톱니바퀴 [Gold 5]
# 회전 하기 전에 다른 톱니들의 2,6번 확인 => 회전 여부+방향 먼저 결정
# 모두 한번에 회전 시키기
import sys
from collections import deque
I = sys.stdin.readline
top = []
result = 0
for _ in range(4):
    top.append(deque(list(I().rstrip())))


def clock(q):
    q.appendleft(q.pop())

def banClock(q):
    q.append(q.popleft())

for _ in range(int(I())):
    check = [0,0,0,0,0]
    a,b = map(int,I().split())

    check[a] = b
    tmp = a
    while True:
        if check[tmp] == 0:
            break

        tmp -= 1
        if tmp < 1:
            break

        if top[tmp][6] != top[tmp-1][2]:
            check[tmp] = (check[tmp+1]*-1)

    tmp = a
    while True:
        if check[tmp] == 0:
            break

        tmp += 1
        if tmp > 4:
            break

        if top[tmp-2][2] != top[tmp-1][6]:
            check[tmp] = (check[tmp-1]*-1)


    for i in range(1,5):
        if check[i] == 1:
            clock(top[i-1])
        elif check[i] == -1:
            banClock(top[i-1])


for i in range(4):
    result += int(top[i][0])*(2**i)

print(result)