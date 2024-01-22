def sinh(a,n,k):
    i = k
    while a[i] == n - k + i and i > 0:
        i -= 1
    if i == 0:
        return
    else:
        a[i] += 1
        for j in range(i+1,k+1,1):
            a[j] = a[j-1] + 1

    
if __name__ == '__main__':
    n,k = map(int,input().split())
    a = [int(i) for i in input().split(' ',n-1)]
    #a = ' '.join(str(i) for i in a)
    se = set()
    cnt = 0
    for i in a:
        se.add(i)
    b = []
    n = len(se)
    for i in range(1,k+1):
        x = i
        b.append(x)
    while True:
        for i in range(1,k+1):
            print(b[i],end=' ')
        print()
        sinh(b,n,k)
    
