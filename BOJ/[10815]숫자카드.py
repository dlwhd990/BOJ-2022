import sys
I = sys.stdin.readline

n = int(I())
myCardList = list(map(int,I().split()))
m = int(I())
yourCardList = list(map(int,I().split()))

myCardList.sort()

start = 0
end = len(myCardList)
r = []

for target in yourCardList:
    result = 0
    start = 0
    end = len(myCardList)
    while start < end:
        mid = (start + end) // 2
        if target == myCardList[mid]:
            result = 1
            break

        elif target > myCardList[mid]:
            start = mid + 1

        elif target < myCardList[mid]:
            end = mid

    r.append(result)

print(*r)