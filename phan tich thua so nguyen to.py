import math

t = int(input())

while t > 0:
    n = int(input())
    s = str(1) + " * "
    a = int(math.sqrt(n))
    cnt = 0
    for i in range(2,a+1):
        if n % i == 0:
            while n % i == 0:
                cnt = cnt + 1
                n = int(n / i)
            s = s + str(i) + "^" + str(cnt) + " * "
            cnt = 0
    if n > 1:
        s = s + str(n) + "^1"
        print(s)
    else:
        m = len(s)
        s1 = s[0:n-3]
        print(s1)

    t = t - 1