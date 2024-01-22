
n, m = map(int, input().split())
a = [[0] * m] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
Max = -1
Min = 10000
for i in range(n):
    for j in range(m):
        Max = max(Max, a[i][j])
        Min = min(Min, a[i][j])
tmp = Max - Min
check = 0
for i in range(n):
    for j in range(m):
        if tmp == a[i][j]:
            check = 1
            break
if check == 1:
    print(tmp)
    for i in range(n):
        for j in range(m):
            if tmp == a[i][j]:
                print('Vi tri ' + '[' + str(i) + ']' + '[' + str(j) +']')
else:
    print('NOT FOUND')

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77