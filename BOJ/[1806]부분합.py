#https://www.acmicpc.net/problem/1806
#부분합 [Gold4]
import sys
I = sys.stdin.readline
n,m = map(int,I().split())
list = list(map(int,I().split()))

left = 0
right = 0
value = list[0]
result = int(1e10)

while left <= right:
    if left == right and value >= m:
        result = 1
        break

    elif value >= m:
        result = min(result,right-left+1)
        value -= list[left]
        left += 1

    elif value < m:
        if right == n-1:
            break
        right += 1
        value += list[right]

if result == int(1e10):
    print(0)
else:
    print(result)