import math
def USC(a,b):
    if b == 0:
        return a
    return USC(b,a % b)

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split(" ",n-1)]
    for i in range(n-1):
        for j in range(i+1,n,1):
            if a[i] > a[j]:
                x = a[i]
                a[i] = a[j]
                a[j] = x
    for i in range(n-1):
        for j in range(i+1,n):
            if USC(a[i],a[j]) == 1:
                print(str(a[i]) + " " + str(a[j]))