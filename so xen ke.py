def check(s):
    n = len(s)
    if n % 2 == 0:
        return False
    if int(s[0]) == int(s[1]):
        return False
    for i in range(n-1,2):
        if int(s[i]) != s[i+2]:
            return False
    return True

if __name__ == '__main__':

    t = int(input())
    while t > 0:
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
        t -= 1
        
