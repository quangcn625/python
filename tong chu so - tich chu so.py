if __name__ == '__main__':
    t = int(input())
    while t > 0:
        s = input()
        n = len(s)
        cntC = 0
        cntL = 0
        sum = 0
        tich = 1
        for i in range(0,n,2):
            cntC = cntC + 1
            sum += int(s[i])
        cntL = n - cntC
        cnt = 0
        for i in range(1,n,2):
            if int(s[i]) == 0:
                cnt = cnt + 1
        if cnt == cntL:
            tich = 0
        else:
            for i in range(1,n,2):
                if int(s[i]) != 0:
                    tich *= int(s[i])
        print(str(sum) +" "+ str(tich))
        t -= 1
