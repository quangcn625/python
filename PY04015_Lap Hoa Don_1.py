
class KhachHang:
    def __init__(self, id, name, csCu, csMoi) -> None:
        self.id = 'KH{0:0>2}'.format(id)
        self.name = name
        self.csCu = csCu
        self.csMoi = csMoi
        soluongnuoc = self.csMoi - self.csCu
        self.tongtien = 0
        if soluongnuoc > 50:
            self.tongtien = 50 * 100
            if soluongnuoc > 100:
                self.tongtien += 50 * 150
                self.tongtien += (soluongnuoc - 100) * 200
                self.tongtien = round(self.tongtien * 1.05)
            else:
                self.tongtien += (soluongnuoc - 50) * 150
                self.tongtien = round(self.tongtien * 1.03)
        else:
            self.tongtien = soluongnuoc * 100 
            self.tongtien = round(self.tongtien * 1.02)

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.tongtien}"

t = int(input())
list = []
for i in range(t):
    name = input()
    csCu = int(input())
    csMoi = int(input())
    list.append(KhachHang(i+1, name, csCu, csMoi))

list.sort(key= lambda x : (-x.tongtien))
for x in list:
    print(x)


'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''
