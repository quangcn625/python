import math

n = int(input())
a = [[0] * n] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
k = int(input())
s1 = 0
s2 = 0
for i in range(n):
    for j in range(i+1, n):
        s1 += a[i][j]
for i in range(n):
    for j in range(0, i):
        s2 += a[i][j]
tmp = int(math.fabs(s1-s2))
if tmp <= k:
    print('YES')
    print(tmp)
else:
    print('NO')
    print(tmp)

# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9