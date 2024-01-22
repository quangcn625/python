
s = input()
a = len(s)
if a % 2 == 0:
    tmp = []
    for i in range(0, a, 2):
        ans = s[i] + s[i+1]
        if ans not in tmp:
            tmp.append(ans)
    tmp.sort()
    print(*tmp)
else:
    tmp = []
    for i in range(0, a-1, 2):
        ans = s[i] + s[i+1]
        if ans not in tmp:
            tmp.append(ans)
    tmp.sort()
    print(*tmp)    

