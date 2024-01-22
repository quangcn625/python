
def check(s):
    n = len(s)
    for i in range(int(n/2)):
        if s[i] != s[n-i-1]:
            return False
    return True

f = open('VANBAN.in', 'r')
List = []
for i in f:
    for j in i.split():
        List.append(j)

Map = {}
tmp = -1
for i in List:
    if check(i):
        tmp = max(tmp, len(i))

for i in List:
    if check(i) and len(i) == tmp:
        if i in Map:
            Map[i] = Map.get(i) + 1
        else:
            Map[i] = 1
for k, v in Map.items():
    print(k, v)
