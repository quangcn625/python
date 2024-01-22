import math
def check(a):
    if a < 2:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = int(input())
        sum = 0
        while s > 0:
            sum = sum + int(s % 10)
            s = s // 10
        if check(sum):
            print("YES")
        else:
            print("NO")

        t -= 1