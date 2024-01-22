
n = int(input())
a = [float(i) for i in input().split()]
x = max(a)
y = min(a)
cnt = 0
sum = 0
for i in range(n):
    if a[i] != x and a[i] != y:
        cnt = cnt + 1
        sum = sum + a[i]
if cnt != 0:
    ans = float(sum / cnt)
    print("{:.2f}".format(ans))
    