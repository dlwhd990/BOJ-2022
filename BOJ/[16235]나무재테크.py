# 나무 재테크 [Gold 3]
import sys,math
from collections import deque
I = sys.stdin.readline

def springSummer(n,land,farm):
    for i in range(n):
        for j in range(n):
            check = 0
            for p in range(len(farm[i][j])):
                if farm[i][j][p] <= land[i][j]:
                    land[i][j] -= farm[i][j][p]
                    farm[i][j][p] += 1

                else:
                    check = len(farm[i][j])-p
                    break

            for p in range(check):
                land[i][j] += math.floor(farm[i][j].pop() / 2)

    # print("SPRING & SUMMER")
    # print(land)
    # print(farm)

def fall(n,farm):
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for i in range(n):
        for j in range(n):
            for p in range(len(farm[i][j])):
                if farm[i][j][p]%5 == 0:
                    for t in range(8):
                        nx = i+dx[t]
                        ny = j+dy[t]
                        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                            continue

                        farm[nx][ny].appendleft(1)

    # print("FALL")
    # print(farm)

def winter(n,land,a):
    for i in range(n):
        for j in range(n):
            land[i][j] += a[i][j]

    # print("WINTER")
    # print(land)



def main():
    result = 0
    n, m, k = map(int, I().split())
    a = []
    farm = [[deque() for _ in range(n)] for _ in range(n)]
    tmp = []
    land = [[5]*n for _ in range(n)]
    for _ in range(n):
        a.append(list(map(int, I().split())))

    for _ in range(m):
        tmp.append(list(map(int, I().split())))

    tmp.sort(key=lambda x: -x[2])

    for x, y, age in tmp:
        farm[x - 1][y - 1].append(age)


    for t in range(k):
        # print(t+1,"년째")
        springSummer(n,land,farm)
        fall(n,farm)
        winter(n,land,a)

        # print("----------")


    for i in range(n):
        for j in range(n):
            result += len(farm[i][j])

    print(result)

main()