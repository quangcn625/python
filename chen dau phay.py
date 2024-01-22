s = input()
n = len(s)

if n < 3:
    print(s)
elif n % 3 == 0:
    for i in range(n):
        if (i+1) % 3 == 0 and (i+1) != n:
            print(s[i]+',',end='')
        else:
            print(s[i],end='')
elif n % 3 == 1:
    print(s[0]+',',end='')
    for i in range(1,n):
        if (i+1) % 3 == 1 and (i+1) != n:
            print(s[i]+',',end='')
        else:
            print(s[i],end='')
elif n % 3 == 2:
    print(s[0]+s[1]+',',end='')
    for i in range(2,n):
        if (i+1) % 3 == 2 and (i+1) != n:
            print(s[i]+',',end='')
        else:
            print(s[i],end='')