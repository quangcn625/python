def USC(a,b):
    if b == 0: return a
    return USC(b , a % b)

def check(a):
    if a < 2:
        return 0
    for i in range(2,a):
        if a % i == 0:
            return 0
    return 1

if __name__ =='__main__':

    t = int(input())

    while t != 0:
        x,y = map(int,input().split())
        a = USC(x,y)
        res = 0
        while a > 0:
            res = res + (a % 10)
            a = int(a/10)
        if check(res) == 1:
            print("YES")
        else:
            print("NO")
        t = t - 1
    
        
    
    
