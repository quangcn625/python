t = int(input())

while t != 0:
    n = input()
    x = len(n)
    a = int(n[0:2])
    b = int(n[x-2:x+1])
    if a==b:
        print("YES")
    else:
        print("NO")

    t = t - 1