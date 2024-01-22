
for i in range(int(input())):
    s1 = input()
    s2 = input()
    print('Test ' + str(i+1) + ': ', end= '')
    if len(s1) != len(s2):
        print('NO')
    else:
        a, b = [], []
        for x in s1:
            a.append(x)
        for x in s2:
            b.append(x)
        a.sort()
        b.sort()
        check = 0
        for x in range(len(a)):
            if a[x] != b[x]:
                check = 1
                break
        if check == 0:
            print('YES')
        else:
            print('NO')
        
# testing
# intestg
# abc
# aabbbcccc
# abcabcbcc
# aabbbcccc
# abc
# xyz