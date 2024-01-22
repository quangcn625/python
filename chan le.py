import math

def check(s):
    sum = 0
    for i in s:
        sum = sum + int(i)
    if sum % 10 != 0:
        return False
    for i in range(len(s)-1):
        if math.fabs(int(s[i])-int(s[i+1])) != 2:
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
    
