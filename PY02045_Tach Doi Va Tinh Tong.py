
a = input()
while True:
    if len(a) == 1:
        break
    b = len(a) // 2
    c = ''
    d = ''
    for i in range(b):
        c += a[i]
    for i in range(b, len(a)):
        d += a[i]
    a = str(int(c) + int(d))
    print(a)
