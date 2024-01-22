t = int(input())

while t != 0:
    s = input()
    n = len(s)
    tmp = ""
    for i in range(n):
        if s[i].isdigit():
            x = int(s[i])
            for j in range(1,x+1):
                print(tmp,end="")
            tmp = ""
        else:
            tmp = tmp + s[i]
    print("\n")
    t = t - 1