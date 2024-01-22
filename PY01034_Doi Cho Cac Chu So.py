
for __ in range(int(input())):
    s = input()
    n = len(s)
    check = 0
    for i in range(n-2, -1, -1):
        if s[i] > s[i+1]:
            check = 1
            tmp = '-1'
            k = -1
            for j in range(i+1, n):
                if s[j] < s[i]:
                    if s[j] > tmp:
                        tmp = s[j]
                        k = j
            s = list(s)
            s[i], s[k] = s[k], s[i]
            s = ''.join(s)
            break
    if check == 0 or s[0] == '0':
        print(-1)
    else:
        print(s)

