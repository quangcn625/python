s = input()
cnt = 0
while len(s) > 1:
    cnt = cnt + 1
    res = 0
    for i in s:
        res = res + (ord(i) - 48)
    s = str(res)
if cnt != 0:
    print(cnt)
else:
    print(1)


    

    