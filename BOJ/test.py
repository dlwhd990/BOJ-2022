a = [1,3,3,5,5,76,78]
b = [[]for _ in range(4)]

b[0].extend(a)
print(b)