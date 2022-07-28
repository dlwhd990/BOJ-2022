#https://www.acmicpc.net/problem/12904
#A와 B [Gold 5]
import sys
I = sys.stdin.readline

a = I().rstrip()
b = I().rstrip()

while len(b) > len(a):
    if b[-1] == 'A':
        b = b[:-1]

    else:
        b = (b[:-1])[::-1]

if a == b:
    print(1)

else:
    print(0)