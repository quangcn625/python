def solve(n,a,b,c):
    if n==1:
        print(str(a) + " -> "+str(c))
    else:
        solve(n-1,a,c,b)
        solve(1,a,b,c)
        solve(n-1,b,a,c)

if __name__ == '__main__':
    n = int(input())
    solve(n,'A','B','C')

