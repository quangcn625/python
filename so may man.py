n = str(input())

cnt1 = 0
cnt2 = 0

for i in n:
    if i == '4':
        cnt1 = cnt1 + 1
    elif i == '7':
        cnt2 = cnt2 + 1

if cnt1 + cnt2 == 4:
    print("YES")
elif cnt1 + cnt2 == 7:
    print("YES")
else:
    print("NO")