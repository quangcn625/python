x,y,z = map(int,input().split())
a = []
i = 1
ok = True
while ok != True:
    if x + i <= z:
        if (x + i) % y == 0:
            a.append(i)
        i = i + 1
    else:
        ok = False
        
print(a)
