t = int(input())

while t > 0:
    x,y,z = map(float,input().split())
    year = 0
    while x < z:
        x = x + x * y / 100
        year += 1
    print(year)
    
    t = t - 1