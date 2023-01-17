# 줄서기 [Gold 5]
import sys
I = sys.stdin.readline
n = int(I())
mainStack = []
for _ in range(n):
    mainStack.extend(list(I().rstrip().split()))

# stack으로 사용하기 위해 reverse
mainStack.reverse()
tmp = sorted(mainStack)
tmp2 = []
order = []

# 문자열로 sort하게 되면 3보다 10이 앞서는 상황이 생기기 때문에
# 문자와 정수 두 부분으로 나누어 정렬한 후 다시 문자열로 합친다.
for i in tmp:
    t = i.split("-")
    tmp2.append([t[0],int(t[1])])

tmp2.sort()

# 다음 입장해야할 사람이 누구인지 판단할 수 있는 order 리스트 완성
for i in tmp2:
    order.append(i[0]+'-'+str(i[1]))

# 문제의 한줄 짜리 대기줄 (= 서브줄)
subStack = []
now = 0
while mainStack or subStack:
    # 만약 서브줄에 사람이 있고, 마지막 사람이 다음번에 들어가야할 사람이라면 입장시킨다
    if len(subStack) > 0 and subStack[-1] == order[now]:
        now += 1
        subStack.pop()

    # 만약 원래 줄의 가장 앞의 사람이 다음번에 들어가야할 사람이라면 입장시킨다.
    elif len(mainStack) > 0 and mainStack[-1] == order[now]:
        now += 1
        mainStack.pop()

    # 앞의 두 경우에 해당하지 않고 원래 줄에 사람이 남아있다면, 원래 줄의 가장 앞 사람을 서브줄로 보낸다.
    elif len(mainStack) > 0:
        subStack.append(mainStack.pop())

    # 원래 줄에 사람이 한명도 없고 서브줄의 맨 뒷사람이 다음번에 입장할 사람이 아닌 경우 => 무조건 불가능
    else:
        break


if len(mainStack) == 0 and len(subStack) == 0 and now == len(order):
    print("GOOD")
else:
    print("BAD")