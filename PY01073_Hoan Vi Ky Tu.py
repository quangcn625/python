import itertools

a = input()
hoanvi = itertools.permutations(a)
for i in hoanvi:
    print(*i, sep='')
