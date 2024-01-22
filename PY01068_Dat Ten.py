import itertools

n, k = map(int, input().split())
s = input().split()
a = []
for i in s:
    if i not in a:
        a.append(i)
a.sort()

tohop = itertools.combinations(a, k)
for i in tohop:
    print(*i)

# 6 2
# DONG TAY NAM BAC TAY BAC
