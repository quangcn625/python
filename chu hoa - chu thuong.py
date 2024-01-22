s = input()

cnt1 = 0
cnt2 = 0
for i in s:
    if i >= 'a' and i <= 'z':
        cnt1 = cnt1 + 1
    elif i >= 'A' and i <= 'Z':
        cnt2 = cnt2 + 1
if cnt1 >= cnt2:
    a = s.lower()
    print(a)
else:
    a = s.upper()
    print(a)