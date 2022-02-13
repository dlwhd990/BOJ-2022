#https://www.acmicpc.net/problem/1316
#그룹 단어 체커 [Silver 5]
import sys
I = sys.stdin.readline

n = int(I())
cnt = 0
for _ in range(n):
    a = list(I().rstrip())
    stack = []

    for i in a:
        if len(stack) == 0 or (stack[-1] != i):
            stack.append(i)

    setStack = list(set(stack))
    stack.sort()
    setStack.sort()
    if ''.join(stack) == ''.join(setStack):
        cnt += 1

print(cnt)