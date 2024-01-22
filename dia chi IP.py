def check(ip):
    cnt = 0
    for i in ip:
        if not i.isdigit() or int(i) > 255 or int(i) < 0: 
            return False
        else:
            cnt += 1
    if cnt != 4:
        return False
    return True

for i in range(int(input())):
    if check(input().split('.')):
        print("YES")
    else:
        print("NO")