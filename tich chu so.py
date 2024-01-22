t = int(input())

while t != 0:
    s = str(input())
    res = 1

    for i in s:
        if i != '0':
            res = res * (int(i))

    print(res)

    t = t - 1