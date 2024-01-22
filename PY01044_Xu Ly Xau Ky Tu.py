

x = input().lower().split()
y = input().lower().split()
se1 = set()
se2 = set()
for i in x:
    se1.add(i)
for i in y:
    se2.add(i)
# Hợp của 2 set
tmp1 = se1 | se2
ans1 = []
for i in tmp1:
    ans1.append(i)
ans1.sort()
# Giao của 2 set
tmp2 = se1 & se2
ans2 = []
for i in tmp2:
    ans2.append(i)
ans2.sort()

print(*ans1)
print(*ans2)


# Lap trinh huong doi tuong
# Ngon ngu lap trinh C++