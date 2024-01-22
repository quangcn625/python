t = int(input())

while t != 0:
    s = input()
    n = len(s)
    a = int(s[n-1])
    b = int(s[0])
    if a == b:
        print("YES")
    else:
        print("NO")
        
    t = t - 1