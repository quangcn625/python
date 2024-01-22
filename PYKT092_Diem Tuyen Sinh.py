
class TuyenSinh:
    def __init__(self, stt, name, diemthi, dantoc, khuvuc) -> None:
        self.id = 'TS{:02d}'.format(stt)
        self.name = self.ChuanHoa(name)
        self.diemthi = diemthi
        self.dantoc = dantoc
        self.khuvuc = khuvuc
        self.uutien = 0
        if self.khuvuc == '1':
            self.uutien = 1.5
        elif self.khuvuc == '2':
            self.uutien = 1
        else:
            self.uutien = 0
        if self.dantoc == 'Kinh':
            self.uutien += 0
        else:
            self.uutien += 1.5
        self.tongdiem = self.diemthi + self.uutien
        self.trangthai = None
        if self.tongdiem >= 20.5:
            self.trangthai = 'Do'
        else:
            self.trangthai = 'Truot'
    
    def ChuanHoa(self, s):
        a = s.strip()
        ans = ''
        for i in a.split():
            ans += i.title() + ' '
        return ans.strip()

    def __str__(self) -> str:
        return '{} {} {:.1f} {}'.format(self.id, self.name, self.tongdiem, self.trangthai)

a = []
for i in range(int(input())):
    a.append(TuyenSinh(i+1, input(), float(input()), input(), input()))

a.sort(key= lambda x : (-x.tongdiem, x.id))
print(*a, sep='\n')

# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3
        
