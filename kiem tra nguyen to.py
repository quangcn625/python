import math
def check(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t != 0:
        s = input()
        n = len(s)
        a = int(s[n-4:n])
        if check(a):
            print("YES")
        else:
            print("NO")

        t -= 1
