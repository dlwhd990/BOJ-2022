# 나만 안되는 연애 [Gold 3]
# point => 부모가 자기 자신인 원소 2개이상? 서로 연결되지 않은 묶음 존재 => 모두 연결이 불가능한 상태
import sys
I = sys.stdin.readline

def main():
    n,m = map(int,I().split())
    result = 0
    gender = list(I().rstrip().split())
    parent = [i for i in range(n+1)]
    routes = []
    for _ in range(m):
        a,b,c = map(int,I().split())
        if gender[a-1] == gender[b-1]:
            continue
        routes.append((a,b,c))

    routes.sort(key=lambda x:x[2])

    def findParent(parent,x):
        if parent[x] != x:
            parent[x] = findParent(parent,parent[x])
        return parent[x]

    def unionParent(parent,a,b):
        a = findParent(parent,a)
        b= findParent(parent,b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b


    for start,end,cost in routes:
        if findParent(parent,start) != findParent(parent,end):
            unionParent(parent,start,end)
            result += cost

    check = 0
    for i in range(1,n+1):
        if i == parent[i]:
            check += 1

        if check > 1:
            return -1

    return result

print(main())

