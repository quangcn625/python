import math

def USC(a,b):
    if b == 0:
        return a
    return USC(b,a%b)

def check_nto(a):
    flag = 1
    if a < 2:
        flag = 0
        return flag
    for i in range(2,a):
        if a % i == 0:
            flag = 0
            break
    return flag

if __name__ == '__main__':

    t = int(input())

    while t != 0:
        n = int(input())

        tmp = 0
        for i in range(1,n):
            if USC(i,n) == 1:
                tmp = tmp + 1
        if check_nto(tmp) == 1:
            print("YES")
        else:
            print("NO")

        t = t - 1

    
    
