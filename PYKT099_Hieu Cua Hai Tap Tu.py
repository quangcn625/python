
f1 = open('DATA1.in', 'r')
se1 = set()
for i in f1:
    for j in i.split():
        se1.add(j.lower())

f2 = open('DATA2.in', 'r')
se2 = set()
for i in f2:
    for j in i.split():
        se2.add(j.lower())

a, b = [], []
for i in se1 - se2:
    a.append(i)
a.sort()
for i in se2 - se1:
    b.append(i)
b.sort()
print(*a)
print(*b)