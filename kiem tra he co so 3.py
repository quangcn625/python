def check(s):
    n = len(s)
    for i in range(n):
        if s[i] != '0' and s[i] != '1' and s[i] != '2':
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
        t = t - 1