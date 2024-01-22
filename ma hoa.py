t = int(input())

while t != 0:
    s = input()
    n = len(s)
    cnt = 1
    for i in range(n-1):
        if s[i]==s[i+1]:
            cnt = cnt + 1
        else:
            print(str(cnt)+s[i],end="")
            cnt = 1
    print(str(cnt)+s[n-1])
    t = t - 1