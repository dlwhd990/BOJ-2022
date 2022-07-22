#https://www.acmicpc.net/problem/11866
#요세푸스 문제 0 [Silver 5]

n,k = map(int,input().split())

a = [i for i in range(1,n+1)]
result = []
idx = 0

while a:
    idx = (idx+(k-1))%len(a)
    result.append(str(a.pop(idx)))

print("<"+', '.join(result)+">")