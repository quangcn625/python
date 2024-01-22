t = int(input())
while t > 0:
    n = int(input())
    s = 0
    sum = 0
    if n % 2 == 0:
        for i in range(2,n+1,2):
            sum = sum + float(1/i)
        ans = "{:.6f}".format(sum)
        print(ans)
    else:
        for i in range(1,n+1,2):
            sum = sum + float(1/i)
        ans = "{:.6f}".format(sum)
        print(ans)
    t -= 1