import math
def check(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
    if check(i):
        b.append(i)
b.sort()
idx = 0
for i in range(n):
    if check(a[i]):
        a[i] = b[idx]
        idx += 1
print(*a)