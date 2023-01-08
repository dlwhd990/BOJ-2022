# 같이 눈사람 만들래? [Gold 3]
import sys
I = sys.stdin.readline
n = int(I())
a = list(map(int,I().split()))
a.sort()

def main():
    result = int(1e9)
    for i in range(n):
        for j in range(i+3,n):
            start = i+1
            end = j-1

            while start < end:
                result = min(result,abs((a[i]+a[j])-(a[start]+a[end])))

                if a[i]+a[j] == a[start]+a[end]:
                    return 0

                if a[i]+a[j] > a[start]+a[end]:
                    start += 1

                elif a[i]+a[j] < a[start]+a[end]:
                    end -= 1

    return result


print(main())