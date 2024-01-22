
map = {}

for i in range(int(input())):
    s = input().lower()
    for x in range(len(s)):
        if not s[x].isalnum():
            s = s.replace(s[x], ' ')
    for x in s.split():
        if x in map:
            map[x] = map.get(x) + 1
        else:
            map[x] = 1

map = sorted(map.items(), key= lambda x : (-x[1], x[0]))
for i in map:
    print(*i)

# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.
