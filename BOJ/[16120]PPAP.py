#https://www.acmicpc.net/problem/16120
#PPAP [Gold 4]
import sys
from collections import deque
I = sys.stdin.readline
q = deque(list(I().rstrip()))
stack = []

while q:
    stack.append(q.popleft())
    if len(stack) > 3 and ''.join(stack[-4:]) == "PPAP":
        for _ in range(3):
            stack.pop()

if len(stack) == 1 and stack[0] == "P":
    print("PPAP")
else:
    print("NP")

