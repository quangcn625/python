
n, m = map(int, input().split())
a, b = [], []
x = input().split()
y = input().split()
if len(x) == n:
    a = [int(i) for i in x]
if len(y) == m:
    b = [int(i) for i in y]
a.sort()
b.sort()
tmp1 = [None] * 1001
tmp2 = [None] * 1001
for i in a:
    tmp1[i] = 1
for i in b:
    tmp2[i] = 1
for i in range(1, 1001):
    if tmp1[i] == 1 and tmp2[i] == 1:
        print(i, end=' ')
print()
for i in range(1, 1001):
    if tmp1[i] == 1 and tmp2[i] != 1:
        print(i, end=' ')
print()
for i in range(1, 1001):
    if tmp2[i] == 1 and tmp1[i] != 1:
        print(i, end=' ')
print()