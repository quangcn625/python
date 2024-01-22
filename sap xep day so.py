for i in range(int(input())):
    n,k = map(int,input().split())
    a = [int(i) for i in input().split()]
    x = max(a)
    idx = int(-1e9)
    for i in range(n):
        if a[i] == x:
            idx = i
    print(idx)
