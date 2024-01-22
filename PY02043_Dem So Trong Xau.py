
for __ in range(int(input())):
    s1 = input()
    s2 = input()
    cnt = 0
    a = len(s1)
    b = len(s2)
    i = 0
    while i <= a:
        if i + b > a:
            break
        x = ''
        for j in range(i, i+b):
            x += s1[j]
        if x == s2:
            cnt += 1
            i = i + b
        else:
            i += 1
    print(cnt)