
class PhongBan:
    def __init__(self, a) -> None:
        self.idPhong = a[0]
        self.namePhong = None
        ans = ''
        for i in range(1,len(a)):
            ans += a[i] + ' '
        self.namePhong = ans.strip()

class NhanVien:
    def __init__(self, ma, name, luongcoban, songaycong, tmp) -> None:
        self.ma = ma
        self.name = name
        self.luongcoban = luongcoban
        self.songaycong = songaycong
        self.tmp = tmp
        x = self.ma[0:1]
        y = int(self.ma[1:3])
        self.luongthang = 0
        if x == 'A':
            if y >= 1 and y <= 3:
                self.luongthang = self.luongcoban * self.songaycong * 10000
            elif y >= 4 and y <= 8:
                self.luongthang = self.luongcoban * self.songaycong * 12000
            elif y >= 9 and y <= 15:
                self.luongthang = self.luongcoban * self.songaycong * 14000
            else:
                self.luongthang = self.luongcoban * self.songaycong * 20000
        elif x == 'B':
            if y >= 1 and y <= 3:
                self.luongthang = self.luongcoban * self.songaycong * 10000
            elif y >= 4 and y <= 8:
                self.luongthang = self.luongcoban * self.songaycong * 11000
            elif y >= 9 and y <= 15:
                self.luongthang = self.luongcoban * self.songaycong * 13000
            else:
                self.luongthang = self.luongcoban * self.songaycong * 16000
        elif x == 'C':
            if y >= 1 and y <= 3:
                self.luongthang = self.luongcoban * self.songaycong * 9000
            elif y >= 4 and y <= 8:
                self.luongthang = self.luongcoban * self.songaycong * 10000
            elif y >= 9 and y <= 15:
                self.luongthang = self.luongcoban * self.songaycong * 12000
            else:
                self.luongthang = self.luongcoban * self.songaycong * 14000
        else:
            if y >= 1 and y <= 3:
                self.luongthang = self.luongcoban * self.songaycong * 8000
            elif y >= 4 and y <= 8:
                self.luongthang = self.luongcoban * self.songaycong * 9000
            elif y >= 9 and y <= 15:
                self.luongthang = self.luongcoban * self.songaycong * 11000
            else:
                self.luongthang = self.luongcoban * self.songaycong * 13000

    def __str__(self) -> str:
        return '{} {} {} {}'.format(self.ma, self.name, self.tmp.namePhong, str(self.luongthang))

a, b = [], []
for i in range(int(input())):
    a.append(PhongBan(list(map(str, input().split()))))

for i in range(int(input())):
    ma = input()
    name = input()
    luongcoban = int(input())
    songaycong = int(input())
    for j in a:
        if ma[3:] == j.idPhong:
            b.append(NhanVien(ma, name, luongcoban, songaycong, j))
            break

print(*b, sep='\n')

# 2
# HC Hanh chinh
# KH Ke hoach Dau tu
# 2
# C06HC
# Tran Binh Minh
# 65
# 25
# D03KH
# Le Hoa Binh
# 59
# 24