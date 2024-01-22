t = int(input())

while t != 0:
    s = input() + "#"
    n = len(s)
    tmp = 0
    res = 1e9
    for i in s:
        if i.isdigit():
            tmp = tmp * 10 + int(i)
        else:
            if tmp > 0:
                res = min(tmp,res)
                tmp = 0
    print(res)

    t = t - 1