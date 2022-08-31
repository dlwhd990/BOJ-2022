#https://www.acmicpc.net/problem/23294
#웹 브라우저 1 [Gold 4]

import sys
from collections import deque
I = sys.stdin.readline

n,m,maxSize = map(int,I().split())
sizes = list(map(int,I().split()))
back = deque()
size = 0
front = []
current = -1
for _ in range(m):
    ipt = list(I().rstrip().split())

    if ipt[0] == 'B':
        if len(back) == 0:
            continue

        front.append(current)
        current = back.pop()

    elif ipt[0] == 'F':
        if len(front) == 0:
            continue

        back.append(current)
        current = front.pop()

    elif ipt[0] == 'A':
        for i in front:
            size -= sizes[i-1]
        front = []
        size += sizes[int(ipt[1])-1]
        if current != -1:
            back.append(current)
            while back and size > maxSize:
                size -= sizes[back.popleft()-1]

        current = int(ipt[1])

    elif ipt[0] == 'C':
        stack = []
        size = 0
        while back:
            stack.append(back.pop())
            if len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()

        while stack:
            back.append(stack.pop())

        for i in back:
            size += sizes[i-1]

        for i in front:
            size += sizes[i-1]

        size += sizes[current-1]

print(current)
back.reverse()
front.reverse()
if len(back) == 0:
    print(-1)
else:
    print(*back)

if len(front) == 0:
    print(-1)

else:
    print(*front)