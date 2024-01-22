
s = input()
k = int(input())
Map = {}
a = len(s)
if a % 2 == 0:
    for i in range(0, a, 2):
        x = s[i] + s[i+1]
        if x in Map:
            Map[x] = Map.get(x) + 1
        else:
            Map[x] = 1
else:
    for i in range(0, a-1, 2):
        x = s[i] + s[i+1]
        if x in Map:
            Map[x] = Map.get(x) + 1
        else:
            Map[x] = 1
Map = dict(sorted(Map.items(), key= lambda x :(x[0])))
Max = max(Map.values())
if k <= Max:
    for ke, va in Map.items():
        if int(va) >= k:
            print(ke, va)
else:
    print('NOT FOUND')