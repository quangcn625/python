flag = 0
while flag == 0:
    n = int(input())
    if n == 0:
        flag = 1
        continue
    a = []
    for i in range(n):
        a.append(int(input()))
    x = max(a)
    y = min(a)
    if x==y:
        print("BANG NHAU")
    else:
        print(y,x)