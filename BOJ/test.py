a = input()
t = [0]*26

for i in a.lower():
    t[ord(i)-97] += 1

for i in range(26):
    t[i] = (t[i],chr(i+65))

t.sort(reverse=True)

if t[1][0] == t[0][0]:
    print("?")

else:
    print(t[0][1])