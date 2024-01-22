t = int(input())

while t > 0:
    s = input()
    ans = ""
    tmp = 0
    for i in range(len(s)-1,0,-1):
        if int(s[i]) + tmp >= 5:
            tmp = 1
        else:
            tmp = 0
        ans = "0" + ans
    ans = str(int(s[0]) + tmp) + ans
    print(ans)
    t = t - 1