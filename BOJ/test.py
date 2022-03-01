n = int(input())

pibo = [0,1]

for i in range(n-1):
    pibo.append(((pibo[-1]%1000000007)+(pibo[-2]%1000000007))%1000000007)

if n == 0:
    print(0)
else:
    print(pibo[-1])