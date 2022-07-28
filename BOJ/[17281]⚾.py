#https://www.acmicpc.net/problem/17281
#⚾ [Gold 4]

import sys
from itertools import permutations as per

def simulation(innings,lineup,results):
    runs = 0
    batter = 0

    for i in range(innings):
        first,second,third = 0,0,0
        outs = 0
        while outs < 3:
            if results[i][lineup[batter]] == 0:
                outs += 1

            elif results[i][lineup[batter]] == 1:
                runs += third
                first,second,third = 1,first,second

            elif results[i][lineup[batter]] == 2:
                runs += (second+third)
                first, second, third = 0, 1, first

            elif results[i][lineup[batter]] == 3:
                runs += (first+second+third)
                first,second,third = 0, 0, 1

            elif results[i][lineup[batter]] == 4:
                runs += (first+second+third+1)
                first,second,third = 0,0,0

            batter += 1
            batter %= 9

    return runs


def main():
    I = sys.stdin.readline
    a = []
    nums = [i for i in range(1,9)]
    innings = int(I())
    for _ in range(innings):
        a.append(list(map(int, I().split())))

    p = list(per(nums, 8))
    result = 0

    for i in p:
        lineup = list(i[0:3]) + [0] + list(i[3:])
        result = max(result, simulation(innings, lineup, a))

    print(result)

main()