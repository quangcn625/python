
t, k = map(int, input().split())
Map = {}

for i in range(t):
    s = input().lower()
    for j in range(len(s)):
        if not s[j].isalnum():
            s = s.replace(s[j], ' ')
    for j in s.split():
        if j in Map:
            Map[j] = Map.get(j) + 1
        else:
            Map[j] = 1

# KHI SORT XONG THÌ MAP TRỜ THÀNH LIST
List = sorted(Map.items(), key= lambda x : (-x[1], x[0]))

for i in List:
    if i[1] >= k:
        print(*i)