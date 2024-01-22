import math
def solve(a):
    res = 1
    while a > 0:
        res = res * (a % 10)
        a = a // 10
    return res
def numer_compare(x):
    return (solve(x),x)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        a = [int(i) for i in input().split()]
        a = sorted(a,key=numer_compare)
        #a.sort(key=numer_compare)
        a = ' '.join(str(i) for i in a)
        print(a)
        t -= 1
