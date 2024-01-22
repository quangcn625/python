def sodao(a):
    s = 0
    while a > 0:
        s = s * 10 + int(a % 10)
        a = int(a / 10)
    return s

def USC(a,b):
    if b == 0:
        return a
    return USC(b,a % b)

if __name__ =='__main__':
    t = int(input())

    while t > 0:
        n = int(input())
        m = sodao(n)
        if(USC(n,m)==1):
            print("YES")
        else:
            print("NO")

        t = t - 1

