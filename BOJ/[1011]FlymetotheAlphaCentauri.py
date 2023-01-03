# Fly me to the Alpha Centauri [Gold 5]

# a[지점] => 지점 까지의 누적합

import sys
I = sys.stdin.readline

a = [0]

for i in range(1,50002):
    a.append(a[-1]+i)

def main():
    x, y = map(int, I().split())
    k = y - x
    for i in range(len(a)-1):  # 구간 어떻게 정할지?
        if a[i]*2 == k:
            return i*2

        if a[i]+a[i+1] == k:
            return i*2+1

        if a[i]+a[i+1] > k:
            if a[i]*2 < k:
                return i*2+1

            else:
                return i*2


for t in range(int(I())):
    print(main())