
def check(s):
    n = len(s)
    if n < 2:
        return False
    for i in range(int(n/2)):
        if s[i] != s[n-i-1]:
            return False
    return True

n, m= map(int, input().split())
a = [[0] * m] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
tmp = -1
for i in range(n):
    for j in range(m):
        if check(str(a[i][j])):
            tmp = max(tmp, a[i][j])
if tmp != -1:
    print(tmp)
    for i in range(n):
        for j in range(m):
            if a[i][j] == tmp:
                print('Vi tri ' + '[' + str(i) + ']' + '[' + str(j) + ']')
else:
    print('NOT FOUND')

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77

