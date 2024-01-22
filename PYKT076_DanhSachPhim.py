import datetime

class TheLoai:
    def __init__(self, stt, nameTL) -> None:
        self.maTL = 'TL{0:0>3}'.format(stt)
        self.nameTL = nameTL
    
class Phim:
    def __init__(self, stt, maTL, ngaykhoichieu, tenphim, sotap, TL) -> None:
        self.maPhim = 'P{0:0>3}'.format(stt)
        self.maTL = maTL
        self.ngaykhoichieu = ngaykhoichieu
        self.tenphim = tenphim
        self.sotap = sotap
        self.TL = TL

    def tenTL(self):
        if self.TL.maTL == self.maTL:
            return self.TL.nameTL

    def __str__(self) -> str:
        return f"{self.maPhim} {self.tenTL()} {self.ngaykhoichieu} {self.tenphim} {self.sotap}"

x, y = [int(x) for x in input().split()]
list1, list2 = [], []
for i in range(x):
    list1.append(TheLoai(i+1, input()))
for i in range(y):
    maTL = input()
    ngaykhoichieu = input()
    tenphim = input()
    sotap = int(input())
    for j in list1:
        if maTL == j.maTL:
            list2.append(Phim(i+1, maTL, ngaykhoichieu, tenphim, sotap, j))
            break

list2.sort(key= lambda x : (datetime.datetime.strptime(x.ngaykhoichieu, '%d/%m/%Y'), x.tenphim, -x.sotap))
for i in list2:
    print(i)

# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5   