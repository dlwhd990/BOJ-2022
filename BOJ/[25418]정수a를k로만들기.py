#https://www.acmicpc.net/problem/25418
#정수 a를 k로 만들기 [Silver 3]
import sys
from collections import deque
I = sys.stdin.readline

distance = [0]*1000001

n,m = map(int,I().split())
q = deque()
q.append(n)

while q:
    x = q.popleft()

    if x+1 <= 1000000 and distance[x+1] == 0:
        distance[x+1] = distance[x] + 1
        q.append(x+1)

    if x*2 <= 1000000 and distance[x*2] == 0:
        distance[x*2] = distance[x] + 1
        q.append(x*2)

print(distance[m])