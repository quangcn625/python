n = int(input())
a = [int(i) for i in input().split(" ",n-1)]
cnt = 0
for i in range(n-1):
    for j in range(i+1,n,1):
        if i < j and a[i] > a[j]:
            cnt += 1
print(cnt)