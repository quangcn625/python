import math

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = [[0] * m] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
Max = -1
for i in range(n):
    for j in range(m):
        if check(a[i][j]):
            Max = max(Max, a[i][j])
if Max != -1:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == Max:
                print('Vi tri ' + '[' + str(i) + ']' + '[' + str(j) +']')
else:
    print('NOT FOUND')

# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29
