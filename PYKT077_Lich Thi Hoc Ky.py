import datetime

class MonHoc:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

class CaThi:
    def __init__(self, stt, a, MH) -> None:
        self.id = 'T{:03d}'.format(stt)
        self.mamon = a[0]
        self.ngaythi = a[1]
        self.giothi = a[2]
        self.nhomthi = a[3]
        self.MH = MH
    
    def __str__(self) -> str:
        return '{} {} {} {} {} {}'.format(self.id, self.mamon, self.MH.name, self.ngaythi, self.giothi, self.nhomthi)

x, y = map(int, input().split())
a, b = [], []

for i in range(x):
    a.append(MonHoc(input(), input()))

for i in range(y):
    c = list(map(str, input().split()))
    for j in a:
        if c[0] == j.id:
            b.append(CaThi(i+1, c, j))
            break

b.sort(key= lambda x : (datetime.datetime.strptime(x.ngaythi, '%d/%m/%Y'), datetime.datetime.strptime(x.giothi, '%H:%M'), x.mamon))
print(*b, sep='\n')

# 2 10
# INT1155
# Tin hoc co so 2
# INT1339
# Ngon ngu lap trinh C++
# INT1155 25/11/2021 08:00 01
# INT1155 04/12/2021 08:00 02
# INT1155 04/12/2021 13:30 03
# INT1155 25/11/2021 13:30 04
# INT1155 25/11/2021 15:00 05
# INT1339 25/11/2021 08:00 01
# INT1339 25/11/2021 08:00 02
# INT1339 04/12/2021 13:30 03
# INT1339 04/12/2021 13:30 04
# INT1339 04/12/2021 15:00 05