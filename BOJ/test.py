n = int(input())
result = [0,0,0]

if n%10 != 0:
    print(-1)
else:
    result[0] = n//300
    n %= 300
    result[1] = n//60
    n %= 60
    result[2] = n//10

    print(*result)