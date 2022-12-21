# IQ Test [Gold 3]
import sys
I = sys.stdin.readline

def main():
    n = int(I())
    a = list(map(int, I().split()))
    stack = []

    if n == 1:
        return 'A'

    if n == 2 :
        if a[0] == a[1]:
            return a[0]
        else:
            return 'A'


    for i in range(2,n):
        if (a[i-2]-a[i-1] == 0):
            tmp = 0
        else:
            tmp = ((a[i-1]-a[i])/(a[i-2]-a[i-1]))

        if (int(tmp) != tmp):
            return 'B'

        if len(stack) > 0 and tmp != stack[-1][0]:
            return 'B'

        if (a[i-1]-tmp*a[i-2]) != (a[i]-tmp*a[i-1]):
            return 'B'

        if int(a[i-1]-tmp*a[i-2]) != (a[i-1]-tmp*a[i-2]):
            return 'B'

        stack.append((tmp,a[i]-tmp*a[i-1]))


    return int(a[-1]*stack[-1][0] + stack[-1][1])

print(main())