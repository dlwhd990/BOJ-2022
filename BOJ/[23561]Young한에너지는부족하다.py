#Young한 에너지는 부족하다 [Silver 2]

import sys
I = sys.stdin.readline

def main():
    n = int(I())
    a = list(map(int, I().split()))

    if n == 1:
        return 0

    a.sort()

    if n % 2 == 0:
        return a[(n * 3 // 2) + (n // 2) - 1] - a[(n * 3 // 2) - (n // 2)]

    else:
        return a[(n * 3 // 2) + (n // 2)] - a[(n * 3 // 2) - (n // 2)]

print(main())