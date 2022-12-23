# 막대기 [Silver 5]
n = int(input())
cnt = 0

while n > 0:
    for i in range(7):
        if n >= 2**(6-i):
            n -= (2**(6-i))
            cnt += 1

print(cnt)