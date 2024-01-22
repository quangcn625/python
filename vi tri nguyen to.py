import math
def nto(a):
    if a < 2 :
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True
def check(s):
    n = len(s)
    for i in range(n):
        if int(s[i]) == 2 or int(s[i]) == 3 or int(s[i]) == 5 or int(s[i]) == 7:
            if nto(i) == False:
                return False
        else:
            if nto(i):
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
