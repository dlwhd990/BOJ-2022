# 문자열 폭발 [Gold 4]
import sys
I = sys.stdin.readline

sentence = I().rstrip()
target = I().rstrip()

stack = []

for i in sentence:
    stack.append(i)
    if len(stack) >= len(target) and ''.join(stack[-len(target):]) == target:
        for _ in range(len(target)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))