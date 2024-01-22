
for __ in range(int(input())):
    x, y, z = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    d = []
    i, j, k = 0, 0 ,0
    while i < x and j < y and k < z:
        if a[i] == b[j] and b[j] == c[k]:
            d.append(a[i])
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j] or a[i] < c[k]:
            i += 1
        elif b[j] < a[i] or b[j] < c[k]:
            j += 1
        else:
            k += 1
    if len(d) != 0:
        print(*d)
    else:
        print('NO')

# 3
# 6 5 8
# 1 5 10 20 40 80
# 5 7 20 80 100
# 3 4 15 20 30 70 80 120
# 3 5 4
# 1 5 5
# 3 4 5 5 10
# 5 5 10 20
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9