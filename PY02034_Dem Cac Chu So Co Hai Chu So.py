
s = input()
Map = {}
a = len(s)
if a % 2 == 0:
    i = 0
    while i < a:
        x = s[i] + s[i+1]
        if x in Map:
            Map[x] = Map.get(x) + 1
        else:
            Map[x] = 1
        i += 2
else:
    i = 0
    while i < a - 1:
        x = s[i] + s[i+1]
        if x in Map:
            Map[x] = Map.get(x) + 1
        else:
            Map[x] = 1
        i += 2
for i in Map.items():
    print(*i)
