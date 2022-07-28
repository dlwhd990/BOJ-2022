#https://www.acmicpc.net/problem/2473
#세 용액 [Gold 3]
#미해결
import sys
I = sys.stdin.readline

n = int(I())
a = list(map(int,I().split()))
a.sort()

start = 0
end = n-1

while True:
 