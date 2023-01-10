# カードシャッフル (Small) [Silver 2]
import sys
I = sys.stdin.readline
for t in range(int(I())):
    m,c,w = map(int,I().split())
    cardList = [i for i in range(m,0,-1)]

    for _ in range(c):
        start,cnt = map(int,I().split())
        stack = []
        target = []

        for i in range(start-1):
            stack.append(cardList.pop())

        for i in range(cnt):
            target.append(cardList.pop())

        while stack:
            cardList.append(stack.pop())

        while target:
            cardList.append(target.pop())


    print("Case #",end="")
    print(t+1,end="")
    print(":",cardList[len(cardList)-w])