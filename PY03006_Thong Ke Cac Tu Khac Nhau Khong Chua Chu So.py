
Map = {}

for t in range(int(input())):
    s = input().lower()
    for i in range(len(s)):
        if not s[i].isalpha():
            s = s.replace(s[i], ' ')
    for i in s.split():
        if i in Map:
            Map[i] = Map.get(i) + 1
        else:
            Map[i] = 1

List = sorted(Map.items(), key= lambda x : (-x[1], x[0]))
for i in List:
    print(*i)