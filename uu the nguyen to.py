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
        cnt1 = 0
        cnt2 = 0
        for i in range(n):
            if check(int(s[i])):
                cnt1 += 1
            else:
                cnt2 += 1
        if check(n) and cnt1 > cnt2:
            print("YES")
        else:
            print("NO")
        t -= 1
