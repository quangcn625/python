
t = int(input())
while t != 0:
    n = input()
    set1 = set()
    cnt = 0
    for i in range(len(n)):
        set1.add(int(n[i]))
    for i in set1:
        cnt = cnt + 1
    if cnt == 2:
        flag = 0
        for i in range(len(n)-2):
            if int(n[i]) != int(n[i+2]):
                flag = 1
                print("NO")
                break
        if flag == 0:
            print("YES")
    else:
        print("NO")
    t = t - 1
