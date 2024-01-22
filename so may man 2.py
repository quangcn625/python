t = int(input())

while t != 0:
    n = str(input())
    flag = 0

    for i in n:
        if i == '4' or i == '7':
            continue
        else:
            flag = 1
            print("NO")
            break

    if flag == 0:
        print("YES")
    t = t - 1