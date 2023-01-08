# 인지융~ [Gold 3]
n = int(input())
a,b = map(int,input().split())
zero = 0
k = [[0]*n for _ in range(n)]
t = [[0]*n for _ in range(n)]

def make():
    cnt = 0
    for i in range(n):
        for j in range(i+1):
            k[i-j][j] = "1"
            cnt += 1
            if cnt == a:
                return

    for i in range(n-1):
        for j in range(1,n-i):
            k[n-j][j+i] = "1"
            cnt += 1
            if cnt == a:
                return


def barricade():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for x in range(n):
        for y in range(n):
            if k[x][y] != "1":
                continue

            t[x][y] = 1
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                    continue

                if k[nx][ny] != "1":
                    t[nx][ny] = 3
                    k[nx][ny] = '0'




make()
barricade()

for i in range(n):
    for j in range(n):
        if t[i][j] == 0:
            k[i][j] = '0'
            zero += 1


if zero >= b:
    print(1)

    cnt = 0
    for i in range(n):
        for j in range(i+1):
            if cnt == b:
                break

            k[n-1-i+j][n-1-j] = "2"
            cnt += 1


        if cnt == b:
            break

    for i in range(n-2):
        for j in range(1,n-i):
            if cnt == b:
                break
            k[n-1-(n-j)][n-1-(i+j)] = "2"
            cnt += 1

        if cnt == b:
            break


    for i in k:
        print(''.join(i))


else:
    print(-1)