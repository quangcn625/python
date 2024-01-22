def solve(a):
    n = len(a)
    if n < 2:
        return 0
    l = a[:n//2]
    r = a[n//2:]
    ans = 0
    ans += solve(l)
    ans += solve(r)

    i=0
    j=0
    k=0
    while i < len(l) and j <len(r):
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
            k += 1
        else:
            a[k] = r[j]
            j += 1
            k += 1
            ans += len(l) - i
    while i < len(l):
        a[k] = l[i]
        k += 1
        i += 1
    while j < len(r):
        a[k] = r[j]
        k += 1
        j += 1
    return ans

n = int(input())
lst = [int(i) for i in input().split()]
print(solve(lst))
