def USC(a,b):
    if b == 0:
        return a
    return USC(b , a % b)

n = int(input())
a = [int(i) for i in input().split()]
for i in range(n-1):
    for j in range(i+1,n):
        if a[i] > a[j]:
            x = a[i]
            a[i] = a[j]
            a[j] = x
for i in range(n-1):
    for j in range(i+1,n):
        if USC(a[i],a[j]) == 1:
            print(a[i],a[j])