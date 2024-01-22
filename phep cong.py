s = input()

res = int(s[0:2]) + int(s[3:5])
tmp = int(s[7:9])
if res == tmp:
    print("YES")
else:
    print("NO")