
for i in range(int(input())):
    s = input() + "#"
    res = -1e9
    tmp = 0
    for i in s:
        if i.isdigit():
            tmp = tmp * 10 + int(i)
        else:
            res = max(tmp,res)
            tmp = 0
    print(res)