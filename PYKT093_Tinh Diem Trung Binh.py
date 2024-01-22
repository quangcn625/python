import math

class SinhVien:
    def __init__(self, stt, name, d1, d2, d3) -> None:
        self.id = 'SV{:02d}'.format(stt)
        self.name = self.ChuanHoa(name)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.diemTB = (d1 * 3 + d2 * 3 + d3 * 2) / 8

    def ChuanHoa(self, s):
        s = s.strip()
        ans = ''
        for i in s.split():
            ans += i.title() + ' '
        return ans.strip()
    
    def __str__(self) -> str:
        return '{} {} {:.2f}'.format(self.id, self.name, math.ceil(self.diemTB * 100) / 100)

a = []
for i in range(int(input())):
    a.append(SinhVien(i+1, input(), int(input()), int(input()), int(input())))

a.sort(key= lambda x : (-x.diemTB, x.id))

Map = {}
Map[a[0].id] = 1
for i in range(1, len(a)):
    if a[i].diemTB == a[i-1].diemTB:
        Map[a[i].id] = Map.get(a[i-1].id)
    else:
        Map[a[i].id] = i + 1

for i in a:
    for j in Map.keys():
        if i.id == j:
            print(i, end=' ')
            print(Map.get(j))
            break


# 3
#  ha Thi kieu     anh
# 7
# 6
# 7
# Pham    THI  HAO
# 6
# 7
# 6
# Le Gia Quang
# 7
# 6
# 7