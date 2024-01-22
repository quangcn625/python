import math

def checkNTo(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = [[0] * m] *n
for i in range(n):
    a[i] = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(m):
        if checkNTo(a[i][j]) and a[i][j] > ans:
            ans = a[i][j]
if ans != 0:
    print(ans)
    for i in range(n):
        for j in range(m):
            if a[i][j] == ans:
                print('Vi tri', end=' ')
                print('[' + str(i) + ']' + '[' + str(j) + ']')
else:
    print('NOT FOUND')

# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29