# 제로 [Silver 4]
import sys
I = sys.stdin.readline
stack = []
for _ in range(int(I())):
    a = int(I())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))