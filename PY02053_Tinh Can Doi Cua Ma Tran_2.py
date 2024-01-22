import math

n = int(input())
a = [[0] * n] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
k = int(input())
s1 = 0
s2 = 0
for i in range(n):
    for j in range(n-i-1):
        s1 += a[i][j]
for i in range(n):
    for j in range(n-i, n):
        s2 += a[i][j]
tmp = int(math.fabs(s1-s2))
if tmp <= k:
    print('YES')
    print(tmp)
else:
    print('NO')
    print(tmp)