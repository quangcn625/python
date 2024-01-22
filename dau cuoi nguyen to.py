import math
def check(a):
    if a < 2 :
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        n = len(s)
        a = int(s[0:3])
        b = int(s[n-3:n])
        if check(a) and check(b):
            print("YES")
        else:
            print("NO")
        t -= 1