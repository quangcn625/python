def USC(a,b):
    if b == 0:
        return a
    return USC(b,a%b)

if __name__ == '__main__':
    x,y = map(int,input().split())
    for i in range(x,y-1):
        for j in range(i+1,y,1):
            for k in range(j+1,y+1,1):
                if USC(i,j)==1 and USC(i,k)==1 and USC(j,k)==1:
                    print("("+str(i)+", "+str(j)+", "+str(k)+")")