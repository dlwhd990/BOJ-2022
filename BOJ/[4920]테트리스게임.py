#테트리스 게임 [Gold 5]
import sys
I = sys.stdin.readline

p = [[(0,0),(0,1),(0,2),(0,3)],[(0,0),(0,1),(1,1),(1,2)],[(0,0),(0,1),(0,2),(1,2)],[(0,0),(0,1),(1,1),(0,2)],[(0,0),(0,1),(1,0),(1,1)]]

def turn(t):
    r = []
    for x,y in t:
        r.append((y,-x))

    return r

round = 0
while True:
    round += 1
    n = int(I())
    if n == 0:
        break

    a = []
    result = -int(1e10)
    for _ in range(n):
        a.append(list(map(int,I().split())))


    for t in range(5):
        z = p[t][:]
        for _ in range(4):
            for i in range(-3, n + 4):
                for j in range(-3, n + 4):
                    tmp = 0
                    check = 0
                    for k in range(4):
                        nx, ny = i + z[k][0], j + z[k][1]
                        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                            check = 1
                            break

                        tmp += a[nx][ny]

                    if check == 0:
                        result = max(result, tmp)

            z = turn(z)

    print(str(round)+".",result)