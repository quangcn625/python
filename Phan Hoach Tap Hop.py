un, a = [], []
r = [0]

def Try(pre, total, index, target, n):
    if total > target:
        return
    if index == 2:
        r[0] += 1
        return
    if total == target:
        Try(0, 0, index + 1, target, n)
        return
    for i in range(pre, n):
        if un[i]:
            un[i] = 0
            Try(i + 1, total + a[i], index, target, n)
            un[i] = 1
    return

T = int(input())

for _ in range(T):
    n = int(input())
    a = sorted(map(int, input().split()))
    SUM = sum(a)
    if SUM % 3 != 0:
        print(0)
    else:
        un = [1] * n
        r = [0]
        Try(0, 0, 0, SUM // 3, n)
        print(r[0])