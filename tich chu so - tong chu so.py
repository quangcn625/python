t = int(input())

while t > 0:
    s = input()
    n = len(s)
    sum = 0
    tich = 1
    for i in range(0,n,2):
        if int(s[i]) != 0:
            tich *= int(s[i])
    for i in range(1,n,2):
        sum += int(s[i])
    print(str(tich) +" "+ str(sum))
    t -= 1