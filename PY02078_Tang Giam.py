
for __ in range(int(input())):
    n = int(input())
    a, b, f, ans = [0] * n, [0] * n, [1] * n, 1
    for i in range(n):
        a[i], b[i] = [float(x) for x in input().split()]
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and b[i] < b[j]:
                f[i] = max(f[i], f[j] + 1)
        ans = max(ans, f[i])
    print(ans)

# 3
# 2
# 1.0 1.0
# 1.5 0.0
# 3
# 1.0 1.0
# 1.0 1.0
# 1.0 1.0
# 6
# 1.5 9.0
# 2.0 2.0
# 2.5 6.0
# 3.0 5.0
# 4.0 2.0
# 10.0 5.5