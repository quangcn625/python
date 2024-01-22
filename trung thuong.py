
for i in range(int(input())):
    a = []
    for k in range(int(input())):
        a.append(input())
    se = set()
    x = 0
    for i in a:
        x = max(x,a.count(i))
    for i in a:
        if a.count(i) == x:
            se.add(i)
    if len(se) == 1:
        print(*se)
    else:
        print(min(se))
        
    