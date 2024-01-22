import math
def USC(a,b):
    if b == 0:
        return a
    return USC(b,a % b)

if __name__ == '__main__':
    n,k = map(int,input().split())
    x = int(math.pow(10,k-1))
    y = int(math.pow(10,k))
    cnt = 0
    for i in range(x,y):
        if(USC(n,i) == 1):
            cnt = cnt + 1
            print(str(i),end=" ")
        if cnt == 10:
            print()
            cnt = 0