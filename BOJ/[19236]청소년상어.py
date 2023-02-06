import sys
from collections import deque

I = sys.stdin.readline
initial = []
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

for _ in range(4):
    tmp = list(map(int,I().split()))
    initial.append([tmp[:2],tmp[2:4],tmp[4:6],tmp[6:]])



def moveFish(state):
    newState = [[]for _ in range(4)]
    for i in range(4):
        for j in range(4):
            newState[i].append(state[i][j][::])
    for n in range(1,17):
        check = 0
        for i in range(4):
            for j in range(4):
                if newState[i][j][0] == n:
                    while True:
                        nx = i+dx[newState[i][j][1]-1]
                        ny = j+dy[newState[i][j][1]-1]

                        if nx < 0 or nx > 3 or ny < 0 or ny > 3:
                            newState[i][j][1] += 1
                            if newState[i][j][1] > 8:
                                newState[i][j][1] = 1
                            continue

                        if newState[nx][ny][0] > 0:
                            tmp = newState[nx][ny]
                            newState[nx][ny] = newState[i][j]
                            newState[i][j] = tmp
                            break

                        else:
                            newState[i][j][1] += 1
                            if newState[i][j][1] > 8:
                                newState[i][j][1] = 1

                    check = 1
                    break

            if check == 1:
                break

    return newState



q = deque()
state = initial[::]
q.append((0,0,state,state[0][0][0]))
# 상어 = 0번 물고기
state[0][0][0] = 0
result = 0
while q:
    x,y,state,score = q.popleft()
    state = moveFish(state)
    possible = []
    shark = state[x][y]
    nx = x
    ny = y
    while True:
        nx += dx[shark[1]-1]
        ny += dy[shark[1]-1]

        if nx < 0 or nx > 3 or ny < 0 or ny > 3:
            break

        if state[nx][ny][0] > 16:
            continue

        possible.append((nx,ny))

    for tx,ty in possible:
        newState = [[]for _ in range(4)]
        for i in range(4):
            for j in range(4):
                newState[i].append(state[i][j][::])
        newState[x][y] = [17,0]
        tmp = newState[tx][ty][0]
        newState[tx][ty][0] = 0
        result = max(result,score+tmp)
        q.append((tx,ty,newState,score+tmp))

print(result)