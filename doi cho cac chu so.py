for __ in range(int(input())):
    s = list(input()) 
    i = len(s) - 2
    while s[i] <= s[i+1] and i >= 0:
        i -= 1
    if i == -1: 
        print(-1)
        continue
    j = len(s) - 1
    while s[i] <= s[j] or s[j] == s[j-1]: 
        j -= 1
    s[i], s[j] = s[j], s[i]
    if s[0] == '0': 
        print(-1)
        continue
    print(*s, sep='')



