import itertools

n, k = map(int, input().split())
a = [int(i) for i in input().split()]
b = []
for i in a:
    if i not in b:
        b.append(i)
b.sort()
tohop = itertools.combinations(b, k)
for i in tohop:
    print(*i)

# 8 3
# 2 4 4 3 5 1 3 4
