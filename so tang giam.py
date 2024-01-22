def check(a):
    c = len(a)
    if c < 3:
        return False
    tmp = 0
    idx = 0
    for i in range(len(a)):
        if int(a[i]) >= tmp:
            tmp = int(a[i])
            idx = i
    n = int(a[0])
    m = int(a[1])
    if(n >= m):
        return False
    else:
        for i in range(2,idx):
            if int(a[i]) <= m:
                return False
            else:
                m = int(a[i])
    x = int(a[len(s)-1])
    y = int(a[len(s)-2])
    if(x >= y):
        return False
    else:
        for i in range(len(a)-3,idx,-1):
            if int(a[i]) <= y:
                return False
            else:
                m = int(a[i])
    return True

if __name__ == '__main__':
    t = int(input())

    while t > 0:
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
        t = t - 1