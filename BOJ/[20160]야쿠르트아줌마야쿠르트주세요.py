# 야쿠르트 아줌마 야쿠르트 주세요 [GOLD 3]
import sys
import heapq as hq

I = sys.stdin.readline

n,m = map(int,I().split())

graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,I().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

route = list(map(int,I().split()))

start = int(I())

def da(s):
    q = []
    hq.heappush(q,(0,s))
    distance = [int(1e10)]*(n+1)
    distance[s] = 0

    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + distance[now]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q,(cost,i[0]))

    return distance

myTime = da(start)

prev = route[0]
yakultTime = [(route[0],0)]
acc = 0
check = 0
for i in range(1,10):
    if check == 0:
        tmpDistance = da(prev)
    check = 0
    if tmpDistance[route[i]] >= int(1e10):
        check = 1
        continue
    acc += tmpDistance[route[i]]
    yakultTime.append((route[i],acc))
    prev = route[i]

result = []
for i in yakultTime:
    if myTime[i[0]] <= i[1]:
        result.append(i[0])

if len(result) == 0:
    print(-1)

else:
    print(min(result))