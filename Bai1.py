def checkND(number):
    if number > 0 and isinstance(number, int):
        return True
    else:
        return False

def nhapdayso(n):
    day_so = []
    cac_so = input().split()
    if len(cac_so) == n:
        day_so = [float(so) for so in cac_so]
    return day_so

def sophantuam(a):
    cnt = 0
    for i in a:
        if i < 0:
            cnt += 1
    return cnt

def TBcong(a):
    s = 0
    cnt = 0
    for i in a:
        if i > 0:
            s += i
            cnt += 1
    return s / cnt


n = input()
while(not checkND(int(n))):
    n = input()
a = nhapdayso(int(n))
print(sophantuam(a))
print(TBcong(a))