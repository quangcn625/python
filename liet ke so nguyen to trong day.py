import math
def check(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
se = set()
for i in a:
    if check(i) and i not in se:
        se.add(i)
        print(i,a.count(i))
       
        