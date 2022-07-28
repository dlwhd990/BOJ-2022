#https://www.acmicpc.net/problem/1475
#방 번호 [Silver 5]
import math

n = input()
t = [0]*10
for i in n:
    t[int(i)] += 1

tmp = t[6]+t[9]
t[6] = math.ceil(tmp/2)
t[9] = math.ceil(tmp/2)

print(max(t))