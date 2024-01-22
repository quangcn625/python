for i in range(int(input())):
    p, q = input().split()
    if p < q:
        x = p
        p = q
        q = x
    s = input().split()
    if len(s)==1:
        x1 = s[0]
        x2 = input()
    else:
        x1 = s[0]
        x2 = s[1]
    s1 = int(x1.replace(p,q))+int(x2.replace(p,q))
    s2 = int(x1.replace(q,p))+int(x2.replace(q,p))
    print(min(s1,s2),max(s1,s2))