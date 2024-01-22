for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    l = a[0]
    r = a[n-1]
    se = set()
    for i in a:
        se.add(i)
    
    cnt = 0
    for i in range(l,r+1):
        if i not in se:
            cnt += 1
    print(cnt)