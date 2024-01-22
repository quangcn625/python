def check(s):
    n = len(s)
    for i in range(n-1):
        if int(s[i+1]) - int(s[i]) < 0:
            return False
    return True

if __name__=="__main__":

    t = int(input())
    while t != 0:
        s = input()
        if(check(s)):
            print("YES")
        else:
            print("NO")
        t = t - 1