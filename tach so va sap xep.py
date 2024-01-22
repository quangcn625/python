a = []
for i in range(int(input())):
    s = input()+'#'
    ans = 0
    flag = 0
    for i in s:
        if i.isdigit():
            ans = ans * 10 + int(i)
            flag = 1
        else:
            if flag == 1:
                a.append(ans)
                flag = 0
            ans = 0
a.sort()
for i in a:
    print(i)
'''
A129h
G07bxjq3
aaaaaaa4aaaa
'''