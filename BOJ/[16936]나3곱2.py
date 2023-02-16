import sys
I = sys.stdin.readline

n = int(I())
a = list(map(int,I().split()))

def find(route,visited):
    if len(route) == n:
        print(*route)
        return True

    for i in range(n):
        if a[i] == route[-1]*2 and visited[i] == 0:
            v = visited[::]
            v[i] = 1
            find(route+[a[i]],v)

        if route[-1]%3 == 0 and a[i] == route[-1]//3 and visited[i] == 0:
            v = visited[::]
            v[i] = 1
            find(route+[a[i]],v)


for i in range(n):
    visited = [0]*n
    visited[i] = 1
    if find([a[i]],visited):
        break