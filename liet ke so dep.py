def check(n):
    if len(n) % 2 != 0:
        return False
    for i in n:
        if int(i) % 2 != 0:
            return False
    for i in 
    return True

t = int(input())

while t > 0:
    a = int(input())
    for i in range(22,a):
        if check(str(i)):
            print(i,end=" ")
    print()
    t -= 1