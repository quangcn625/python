for i in range(int(input())):
    s = input()
    a = []
    sum = 0
    for i in s:
        if i.isdigit():
            sum = sum + int(i)
        else:
            a.append(i)
    a.sort()
    res = ""
    for i in a:
        res = res + i
    print(res + str(sum))

