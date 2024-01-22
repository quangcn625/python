
for __ in range(int(input())):
    s = input()
    a = []
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
            a.append(cnt)
            print(cnt, end= ' ')
        elif i == ')':
            print(a[-1], end= ' ')
            a.pop()
    print()
        