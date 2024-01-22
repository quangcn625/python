import math

t = int(input())
while t != 0:
    s1 = input()
    #lật ngược lại mảng
    s2 = s1[::-1]
    n = len(s1)
    flag = 0
    for i in range(1,n):
        x1 = ord(s1[i])
        y1 = ord(s1[i-1])
        x2 = ord(s2[i])
        y2 = ord(s2[i-1])
        if math.fabs(x1-y1) != math.fabs(x2-y2):
            flag = 1
            print("NO")
            break
    if flag == 0:
        print("YES")

    t -= 1
