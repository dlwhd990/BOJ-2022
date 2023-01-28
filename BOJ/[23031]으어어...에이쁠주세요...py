# 으어어… 에이쁠 주세요.. [Gold 4]
import sys
I = sys.stdin.readline

n = int(I())
a = []
zom = []
sx = [-1,-1,-1,0,0,0,1,1,1]
sy = [-1,0,1,-1,0,1,-1,0,1]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ari = [0,0]

move = list(I().rstrip())
for _ in range(n):
    a.append(list(I().rstrip()))

for i in range(n):
    for j in range(n):
        if a[i][j] == 'Z':
            zom.append([i,j,0])
            a[i][j] = 'O'

def simulation():
    d = 2
    for m in move:
        if m == 'F':
            ari[0] += dx[d]
            ari[1] += dy[d]

            if ari[0] < 0:
                ari[0] = 0
            elif ari[0] > n-1:
                ari[0] = n-1

            if ari[1] < 0:
                ari[1] = 0
            elif ari[1] > n-1:
                ari[1] = n-1

        elif m == "L":
            if d == 0:
                d = 3
            else:
                d -= 1

        elif m == "R":
            if d == 3:
                d = 0
            else:
                d += 1


        if a[ari[0]][ari[1]] == "S":
            for i in range(9):
                if 0 <= ari[0]+sx[i] <= n-1 and 0 <= ari[1]+sy[i] <= n-1 and a[ari[0]+sx[i]][ari[1]+sy[i]] == 'O':
                    a[ari[0]+sx[i]][ari[1]+sy[i]] = "K"

        for i in range(len(zom)):
            if zom[i][0] == ari[0] and zom[i][1] == ari[1] and a[ari[0]][ari[1]] == 'O':
                return False

            # 아래를 보고 있는 경우
            if zom[i][2] == 0:
                if zom[i][0] == n-1:
                    zom[i][2] = 1
                else:
                    zom[i][0] += 1

            elif zom[i][2] == 1:
                if zom[i][0] == 0:
                    zom[i][2] = 0
                else:
                    zom[i][0] -= 1

            if zom[i][0] == ari[0] and zom[i][1] == ari[1] and a[ari[0]][ari[1]] == 'O':
                return False

    return True

result = simulation()
if result:
    print("Phew...")
else:
    print("Aaaaaah!")