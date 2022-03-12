# 수 이어 쓰기 1 [Silver 3]

n = int(input())

result = 0

m = 0
for i in range(8,-1,-1):
    if n // pow(10,i) > 0:
        m = i
        break


for i in range(1,m+1):
    result += 9*i*pow(10,i-1)

print(result+(n-pow(10,m)+1)*(m+1))