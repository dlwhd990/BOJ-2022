import sys
I = sys.stdin.readline
n = int(I())
r = []
for _ in range(n):
    a = float(I())
    r.append(a)

r.sort()
for i in range(7):
    print("{:.3f}".format(r[i]))