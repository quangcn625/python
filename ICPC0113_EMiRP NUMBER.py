import math

def checkNTo(n):
    if n < 2 :
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def TN(n):
    ans = 0
    while n != 0:
        ans = ans * 10 + n % 10
        n = n // 10
    return ans

for __ in range(int(input())):
    n = int(input())
    Map = {}
    for i in range(13, n+1):
        if checkNTo(i) and checkNTo(TN(i)) and i != TN(i) and TN(i) < n:
            if (i and TN(i)) in Map:
                continue
            else:
                x = TN(i)
                Map[i] = 1
                Map[x] = 1
    for K in Map.keys():
        print(K, end= ' ')
    print()