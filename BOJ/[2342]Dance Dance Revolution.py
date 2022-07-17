#https://www.acmicpc.net/problem/2342
#Dance Dance Revolution [Gold 3]
import sys
I = sys.stdin.readline

commandList = list(map(int,I().split()))

dp = [[[int(1e10)]*5 for _ in range(5)]for _ in range(len(commandList)-1)]

if len(commandList) > 1:
    dp[0][commandList[0]][0] = 2
    dp[0][0][commandList[0]] = 2

for i in range(1,len(commandList)-1):
    for left in range(5):
        for right in range(5):
            if dp[i-1][left][right] != int(1e10):
                if left == 0:
                    dp[i][commandList[i]][right] = min(dp[i][commandList[i]][right], dp[i-1][left][right] + 2)

                elif left == commandList[i]:
                    dp[i][commandList[i]][right] = min(dp[i][commandList[i]][right], dp[i-1][left][right] + 1)

                elif abs(left-commandList[i]) != 2:
                    dp[i][commandList[i]][right] = min(dp[i][commandList[i]][right], dp[i-1][left][right] + 3)

                elif abs(left-commandList[i]) == 2:
                    dp[i][commandList[i]][right] = min(dp[i][commandList[i]][right], dp[i-1][left][right] + 4)

                if right == 0:
                    dp[i][left][commandList[i]] = min(dp[i][left][commandList[i]], dp[i-1][left][right] + 2)

                elif right == commandList[i]:
                    dp[i][left][commandList[i]] = min(dp[i][left][commandList[i]], dp[i-1][left][right] + 1)

                elif abs(right-commandList[i]) != 2:
                    dp[i][left][commandList[i]] = min(dp[i][left][commandList[i]], dp[i-1][left][right] + 3)

                elif abs(right-commandList[i]) == 2:
                    dp[i][left][commandList[i]] = min(dp[i][left][commandList[i]], dp[i-1][left][right] + 4)

result = int(1e10)

if len(commandList) > 1:
    for i in dp[-1]:
        result = min(result,min(i))

    print(result)

else:
    print(1)