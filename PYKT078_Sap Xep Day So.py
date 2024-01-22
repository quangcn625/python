for i in range(int(input())):
    n,k = map(int,input().split())
    a, b, c1, c2 = [], [], [], []
    a = [int(i) for i in input().split()]
    tmp = -1e9
    idx = -1
    for i in range(n):
        if tmp < a[i]:
            tmp = a[i]
            idx = i
    for i in range(idx):
        b.append(a[i])
    b.append(k)
    for i in range(idx, n):
        b.append(a[i])
    for i in b:
        if i < 0:
            c1.append(i)
        else:
            c2.append(i)
    print(*c1, end=' ')
    print(*c2)

# 1
# 5 3
# -1 2 3 4 -1
