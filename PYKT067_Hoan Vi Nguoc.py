import itertools

for __ in range(int(input())):
    n = int(input())
    a, b = [], []
    for i in range(1, n+1):
        a.append(i)
    hoanvi = itertools.permutations(a)
    for i in hoanvi:
        b.append(i)
    print(len(b))
    b.reverse()
    for i in b:
        ans = ''
        for j in i:
            ans += str(j)
        print(ans, end=' ')
    print()