#https://www.acmicpc.net/problem/14500
#테트리미노 [Gold 5]

import sys
I = sys.stdin.readline

#90도 회전 함수
def turn(idxList):
    result = []
    for x, y in idxList:
        result.append((y, -x))

    return result

def scoreChecker(idxList,stage,n,m,turnMino):
    result = 0
    for _ in range(4):
        for i in range(n):
            for j in range(m):
                tmp = 0
                for dx, dy in idxList:
                    nx = i + dx
                    ny = j + dy

                    if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                        break

                    tmp += stage[nx][ny]

                result = max(result, tmp)

        idxList = turnMino(idxList)

    return result



# 메인
def main():
    n, m = map(int, I().split())
    stage = []
    result = 0
    for _ in range(n):
        stage.append(list(map(int, I().split())))

    minos = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (0, 1), (1, 1), (1, 0)], [(0, 0), (1, 0), (2, 0), (2, 1)],
             [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (1, 1), (0, 2)],[(0,0),(1,0),(2,0),(2,-1)],[(0,0),(1,0),(1,-1),(2,-1)]]


    for mino in minos:
        result = max(result,scoreChecker(mino,stage,n,m,turn))

    print(result)

# 실행
main()