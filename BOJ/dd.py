
# 자물쇠 문제 TC 생성용

import sys
from collections import deque
I = sys.stdin.readline

n = int(I())
push1 = int(I())
start,end = map(int,I().split())
push2 = int(I())

q = deque([i for i in range(1,n+1)])

for _ in range(push1):
    q.append(q.popleft())

# print("ONE", *q)
q = deque(list(q)[:start-1] + list(q)[start-1:end][::-1] + list(q)[end:])

# print("GUG", *q)

for _ in range(push2):
    q.append(q.popleft())

# print("TWO",*q)

print(*q)