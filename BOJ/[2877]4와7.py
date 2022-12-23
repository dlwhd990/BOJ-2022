# 4와 7 [Gold 5]
import sys
I = sys.stdin.readline

n = int(I())
tmp = 0
length = 1
r = 0
result = ''
while True:
    tmp += 2**length

    if (tmp < n):
        length += 1

    else:
        r = (n-2**length+1)
        break


for i in range(length):
    tmp = ((r//2**i)%2)%2
    if tmp == 0:
        result += '4'
    else:
        result += '7'

print(result[::-1])