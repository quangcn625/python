import math

def check(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def dao(n):
    ans = 0
    sum = 0
    while n > 0:
        a = int(n % 10)
        if check(a) ==  False:
            return False
        ans = ans * 10 + a
        sum = sum + a
        n //= 10
    if check(ans) ==  False:
        return False
    if check(sum) == False:
        return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        sum = 0

        if check(n) and dao(n):
            print("Yes")
        else:
            print("No")
        t -= 1