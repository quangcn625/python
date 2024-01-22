import math
def fb(n):
    f = [None]*100
    f[1] = 1
    f[2] = 1
    i = 3
    while i <= 92:
        f[i] = f[i-1] + f[i-2]
        i = i + 1
    return f[n]


t = int(input())

while t > 0:
    n,m = map(int,input().split())
    for i in range(n,m+1):
        print(fb(i),end=" ")
    print()
    t = t - 1
      