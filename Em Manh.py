def check(n):
    sum = 0
    a = n
    while n > 0:
        x = n % 10
        sum = sum + x ** 3
        n = n // 10
    if sum != a:
        return False
    return True

a = []
for i in range(100,1001):
    if check(i):
        a.append(i)
print(*a)