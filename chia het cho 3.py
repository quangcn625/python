t = int(input())

while t != 0:
    s = str(input())

    sum = 0
    for i in s:
        a = int(i)
        sum = sum + a
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")

    t = t - 1