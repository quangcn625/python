
n, m = map(int, input().split())
x = input().split()
y = input().split()
a, b = [], []
if len(x) == n:
    a = [int(i) for i in x]
if len(y) == m:
    b = [int(i) for i in y]

ans1, ans2 = [], []
for i in a:
    if i not in ans1:
        ans1.append(i)
for i in b:
    if i not in ans2:
        ans2.append(i)
if len(ans1) == len(ans2):
    check = 0
    for i in range(len(ans1)):
        if ans1[i] != ans2[i]:
            check = 1
            print('NO')
            break
    if check == 0:
        print('YES')
else:
    print('NO')

# 12 18
# 1 2 3 4 5 1 2 3 5 4 1 2
# 1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5