#https://www.acmicpc.net/problem/15312
#이름 궁합 [Silver 5]
import sys
I = sys.stdin.readline

me = I().rstrip()
her = I().rstrip()
r = []

counts = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

total = ""

for i in range(len(me)):
    total += me[i]
    total += her[i]

for i in total:
    r.append(counts[ord(i)-65])


while len(r) > 2:
    tmp = []
    for i in range(1,len(r)):
        tmp.append(int(str(r[i-1]+r[i])[-1]))

    r = tmp

print(str(r[0])+str(r[1]))