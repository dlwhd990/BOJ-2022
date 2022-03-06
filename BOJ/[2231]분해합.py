# 분해합 [Bronze 2]
n = int(input())

result = 0
for i in range(1,n):
    r = i

    for j in str(i):
        r += int(j)

    if r == n:
        result = i
        break

print(result)