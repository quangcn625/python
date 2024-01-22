import math
def nto(n):
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
        cnt1 = 0
        cnt2 = 0
        for i in range(len(s)):
            if nto(int(s[i])):
                cnt1 += 1
            else:
                cnt2 += 1
        if nto(len(s)) and cnt1 > cnt2:
            print("YES")
        else:
            print("NO")
        
        t -= 1