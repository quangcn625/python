
def USC(a, b):
    if b==0:
        return a
    return USC(b, a%b)

for __ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.sort()
    tmp = 1
    b = []
    for i in a:
        if USC(tmp, i) == k: