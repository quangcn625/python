t = int(input())

while t != 0:
    x,y = map(int,input().split())
    a = [int(i) for i in input().split(" ", x-1)]
    ans1 = []
    ans2 = []

    for i in range(y):
        ans1.append(a[i])
    for i in range(y,x):
        ans2.append(a[i])

    s1 = ' '.join(str(x) for x in ans1)
    s2 = ' '.join(str(x) for x in ans2)

    print(s2 + ' ' + s1)

    t = t - 1