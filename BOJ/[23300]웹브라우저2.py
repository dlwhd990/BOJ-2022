#https://www.acmicpc.net/problem/23300
#웹 브라우저 2 [Gold 5]
import sys
I = sys.stdin.readline

n,m = map(int,I().split())
back = []
front = []
current = -1
for _ in range(m):
    ipt = list(I().rstrip().split())
    if ipt[0] == 'B':
        if current == -1:
            continue

        if len(back) == 0:
            continue

        front.append(current)
        current = back.pop()

    elif ipt[0] == 'F':
        if current == -1:
            continue

        if len(front) == 0:
            continue

        back.append(current)
        current = front.pop()

    elif ipt[0] == "A":
        if current != -1:
            back.append(current)
        front = []
        current = int(ipt[1])

    elif ipt[0] == 'C':
        stack = []
        while back:
            stack.append(back.pop())

            if len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()

        while stack:
            back.append(stack.pop())

back.reverse()
front.reverse()
print(current)
if len(back) == 0:
    print(-1)
else:
    print(*back)

if len(front) == 0:
    print(-1)
else:
    print(*front)