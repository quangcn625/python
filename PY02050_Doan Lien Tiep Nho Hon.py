
for __ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    b.append(1)
    for i in range(1, n):
        cnt = 1
        for j in range(i-1, -1, -1):
            if a[j] <= a[i]:
                cnt += 1
            else:
                break
        b.append(cnt)
    print(*b)
        