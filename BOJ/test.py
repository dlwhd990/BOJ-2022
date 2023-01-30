import sys
I = sys.stdin.readline

result = 0
a,b,c = map(int,I().split())
x,y,z = map(int,I().split())

if a >= x:
    result += x
    a -= x
    x = 0

else:
    result += a
    x -= a
    a = 0

if b >= y:
    result += y
    b -= y
    y = 0

else:
    result += b
    y -= b
    b = 0


if c >= z:
    result += z
    c -= z
    z = 0

else:
    result += c
    z -= c
    c = 0

