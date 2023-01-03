# 자물쇠 [Gold 1]

# 연속하지 않는 수 (양 끝 제외)들이 연속되는 경우? => 그 사이에서 뒤집기가 일어났다.
# 1~끝, 1~끝-1, 시작+1~끝 => 내 방식으로는 해결 안됨 (시작, 끝점 중 하나 이상이 극에 있는 경우)
import sys
from collections import deque
I = sys.stdin.readline

n = int(I())
a = list(map(int,I().split()))
q = deque(a)

check = -1
hubo = []
for t in range(1,n):
    q.appendleft(q.pop())
    r = []
    for i in range(1, n):
        tmp = abs(q[i-1]-q[i])
        if tmp != 1 and tmp != n-1:
            r.append(i)

    if len(r) == 2:
        hubo.append([r[0]+1,r[1],t])




for x,y,t in hubo:
    q = deque(a)
    for _ in range(t):
        q.appendleft(q.pop())
    q = deque(list(q)[:x-1] + list(q)[x-1:y][::-1] + list(q)[y:])
    check = -1
    for k in range(1,n):
        q.appendleft(q.pop())
        if q[0] == 1 and q[-1] == n:
            check = k
            break

    if check > 0:
        print(check)
        print(x,y)
        print(t)
        break


if check == -1:
    for i in range(1,n):
        q.appendleft(q.pop())

        if q[0] == n and q[-1] == 1:
            check = i

    print(1)
    print(1,n)
    print(check)



'''
# [암호화 <=> 복호화 결과 일치하는 지 확인하는 파일]
import sys
from collections import deque
I = sys.stdin.readline

a = list(map(int,I().split()))
n = len(a)

def main():
    q = deque(a)
    check = -1
    hubo = []
    for t in range(1, n):
        q.appendleft(q.pop())
        r = []
        for i in range(1, n):
            tmp = abs(q[i - 1] - q[i])
            if tmp != 1 and tmp != n - 1:
                r.append(i)

        if len(r) == 2:
            hubo.append([r[0] + 1, r[1], t])

    for x, y, t in hubo:
        q = deque(a)
        for _ in range(t):
            q.appendleft(q.pop())
        q = deque(list(q)[:x - 1] + list(q)[x - 1:y][::-1] + list(q)[y:])
        check = -1
        for k in range(1, n):
            q.appendleft(q.pop())
            if q[0] == 1 and q[-1] == n:
                check = k
                break

        if check > 0:
            print(check)
            print(x, y)
            print(t)
            return [check,x,y,t]

    if check == -1:
        for i in range(1, n):
            q.appendleft(q.pop())

            if q[0] == n and q[-1] == 1:
                check = i

        print(1)
        print(1, n)
        print(check)
        return [1,1,n,check]


def make(push1,start,end,push2):
    q = deque([i for i in range(1, n + 1)])

    for _ in range(push1):
        q.append(q.popleft())

    # print("ONE", *q)
    q = deque(list(q)[:start - 1] + list(q)[start - 1:end][::-1] + list(q)[end:])

    # print("GUG", *q)

    for _ in range(push2):
        q.append(q.popleft())

    # print("TWO", *q)
    if a == list(q):
        print(True)


make(*main())
'''

'''
# 자물쇠 문제 TC 생성용

import sys
from collections import deque
I = sys.stdin.readline

n = int(I())
push1 = int(I())
start,end = map(int,I().split())
push2 = int(I())

q = deque([i for i in range(1,n+1)])

for _ in range(push1):
    q.append(q.popleft())

# print("ONE", *q)
q = deque(list(q)[:start-1] + list(q)[start-1:end][::-1] + list(q)[end:])

# print("GUG", *q)

for _ in range(push2):
    q.append(q.popleft())

# print("TWO",*q)

print(*q)
'''