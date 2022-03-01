# 1로 만들기 [Silver 3]

n = int(input())

d = [int(1e10)]*1000001
d[1] = 0

for i in range(1,1000001):
    if i*3 < 1000001:
        d[i*3] = min(d[i] + 1,d[i*3])

    if i*2 < 1000001:
        d[i*2] = min(d[i] + 1,d[i*2])

    if i+1 < 1000001:
        d[i+1] = min(d[i] + 1,d[i+1])


print(d[n])