# 좌표 정렬하기 2 [Silver 5]
import sys
I = sys.stdin.readline
n = int(I())
spots = []

for _ in range(n):
    x,y = map(int,I().split())
    spots.append((x,y))

spots.sort(key=lambda x:(x[1],x[0]))

for spot in spots:
    print(*spot)