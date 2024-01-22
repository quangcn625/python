import math

class SinhVien:
    def __init__(self, id, name, p) -> None:
        self.id = "HS" + "{:02d}".format(id)
        self.name = name
        self.diemTB = p[0] * 2.0 + p[1] * 2.0
        for i in range(2, 10):
            self.diemTB += p[i]
        self.diemTB = self.diemTB / 12
        if self.diemTB >= 9.0:
            self.xepLoai = "XUAT SAC"
        elif self.diemTB >= 8.0:
            self.xepLoai = "GIOI"
        elif self.diemTB >= 7.0:
            self.xepLoai = "KHA"
        elif self.diemTB >= 5.0:
            self.xepLoai = "TB"
        else:
            self.xepLoai = "YEU"

    def __str__(self) -> str:
        return "{} {} {:.1f} {}".format(self.id, self.name, round(self.diemTB + 0.01, 1), self.xepLoai)

def cmp(a):
    return (a.diemTB, (-1) * a.id)

List = []

for i in range(int(input())):
    List.append(SinhVien(i + 1, input(), list(map(float, input().split()))))

List.sort(key= cmp, reverse=True)
for i in List:
    print(i)

'''
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
Le Gia Quang
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
'''