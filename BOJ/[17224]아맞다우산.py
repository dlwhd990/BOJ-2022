#https://www.acmicpc.net/problem/17244
#아맞다우산 [Gold 2]
import sys
from collections import deque
from itertools import permutations as per
I = sys.stdin.readline

#추가: 물건이 하나도 없을 경우 시작점부터 문까지의 거리 계산
def goDoor(start,end,ground):
    n = len(ground)
    m = len(ground[0])
    q = deque()
    q.append(start)
    distance = [[0] * len(ground[0]) for _ in range(len(ground))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue

            if ground[nx][ny] != '#' and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                if end[0] == nx and end[1] == ny:
                    return distance[nx][ny]
                q.append((nx, ny))

    return distance


#시작점과 물건들 간의 거리 + 문과 물건들 간의 거리 계산
def calcFromStartAndDoor(start,ground):
    n = len(ground)
    m = len(ground[0])
    q = deque()
    q.append(start)
    distance = [[-1] * len(ground[0]) for _ in range(len(ground))]
    distance[start[0]][start[1]] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue

            if ground[nx][ny] != '#' and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

    return distance


#물건 간의 거리 계산
def calcDistance(start,end,ground):
    n = len(ground)
    m = len(ground[0])
    q = deque()
    q.append(start)
    distance = [[0]*len(ground[0]) for _ in range(len(ground))]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue

            if ground[nx][ny] != "#" and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                if nx == end[0] and ny == end[1]:
                    return distance[nx][ny]
                q.append((nx,ny))



#calcDist함수를 실행하여 물건들 간의 거리 그래프 제작
def makeGraph(items,ground):
    graph = [[0] * len(items) for _ in range(len(items))]


    for i in range(len(items)):
        for j in range(i+1,len(items)):
            dist = calcDistance(items[i],items[j],ground)
            graph[i][j] = dist
            graph[j][i] = dist


    return graph

#종합된 경우의 수들을 가지고 최종 결과 계산
def makeResult(n,startDist,endDist,distance):
    p = [i for i in range(n)]
    permutations = list(per(p,n))
    result = int(1e10)

    for i in permutations:
        tmp = startDist[i[0]]
        for j in range(1,n):
            tmp += distance[i[j-1]][i[j]]

        result = min(result,tmp+endDist[i[-1]])

    return result


#메인
def main():
    m,n = map(int,I().split())
    ground = []
    s = -1
    e = -1
    for _ in range(n):
        ground.append(list(I().rstrip()))

    items = []

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 'X':
                items.append((i,j))

            elif ground[i][j] == 'S':
                s = (i,j)

            elif ground[i][j] == 'E':
                e = (i,j)

    if len(items) == 0:
        print(goDoor(s,e,ground))
        return

    startDist = [0]*len(items)
    doorDist = [0]*len(items)

    tmp = calcFromStartAndDoor(s, ground)
    for k in range(len(items)):
        startDist[k] = tmp[items[k][0]][items[k][1]]

    tmp = calcFromStartAndDoor(e, ground)
    for k in range(len(items)):
        doorDist[k] = tmp[items[k][0]][items[k][1]]


    graph = makeGraph(items,ground)
    print(makeResult(len(items),startDist,doorDist,graph))
    return

#실행
main()