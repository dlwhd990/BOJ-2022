from collections import deque

a = deque()
a.append(1)
a.append(2)
a.append(3)
a = a[1:]
print(a)