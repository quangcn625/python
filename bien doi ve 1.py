flag = 1
while flag == 1:
    n = int(input())
    if n == 0:
        flag = 0
        continue
    cnt = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            cnt = cnt + 1
        else:
            n = n * 3 + 1
            cnt = cnt + 1
    print(cnt)

