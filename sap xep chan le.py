n = int(input())
a = []
while len(a) < n:
    a += [int(i) for i in input().split()]
tmp1 = []
tmp2 = []
for i in a:
    if i % 2 == 0:
        tmp1.append(i)
    else:
        tmp2.append(i)
tmp1.sort()
tmp2.sort()
cnt1 = 0
cnt2 = len(tmp2)-1
for i in range(n):
    if a[i] % 2 == 0:
        print(tmp1[cnt1],end=' ')
        cnt1 += 1
    else:
        print(tmp2[cnt2],end=' ')
        cnt2 -= 1
