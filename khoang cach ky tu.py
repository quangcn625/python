import math

t = int(input())

while t != 0:
    s1 = input()
    n = len(s1)
    s2 = ""
    for i in range(n-1,-1,-1):
        s2 = s2 + s1[i]
    flag = 1
    for i in range(1,n):
        '''ord : bien ky tu thanh ma ascii'''
        x1 = int(ord(s1[i]))
        y1 = int(ord(s1[i-1]))
        x2 = int(ord(s2[i]))
        y2 = int(ord(s2[i-1]))
        if math.fabs(x1-y1) != math.fabs(x2-y2):
            flag = 0
            print("NO")
            break
    if flag == 1:
        print("YES")

    t = t-1