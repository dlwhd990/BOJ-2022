# RBY팡! [Gold 2]
import sys
I = sys.stdin.readline
n = int(I())
a = []
for _ in range(n):
    a.append(int(I()))

def main():
    if n < 4:
        return n

    possible = []
    result = n
    for i in range(4,n):
        check = [0,0,0]
        for j in range(i-4,i):
            check[a[j]-1] += 1

        if check.count(3) == 1 and check.count(1) == 1:
            possible.append((a[i-4:i].index(check.index(1)+1)+i-4,check.index(3)+1))


    possible = list(set(possible))

    for position,changeTo in possible:
        stack = []
        check = -1
        for i in range(n):
            if position == i:
                stack.append(changeTo)

            else:
                stack.append(a[i])


            if check != -1 and stack[check] != stack[-1]:
                tmp = stack[-1]
                for _ in range(check,len(stack)):
                    stack.pop()
                stack.append(tmp)
                check = -1

            if check == -1 and len(stack) > 3 and stack[-1] == stack[-2] == stack[-3] == stack[-4]:
                check = len(stack)-4


            if i == n-1 and check != -1:
                for _ in range(check,len(stack)):
                    stack.pop()

        result = min(result,len(stack))

    return result

print(main())