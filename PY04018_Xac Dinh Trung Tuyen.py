
class GiaoVien:
    def __init__(self, stt, name, maXT, diemTH, diemCM) -> None:
        self.id = 'GV{0:0>2}'.format(stt)
        self.name = name
        self.maXT = maXT
        self.diemTH = diemTH
        self.diemCM = diemCM
        x = self.maXT[0:1]
        self.mon = None
        if x == 'A':
            self.mon = 'TOAN'
        elif x == 'B':
            self.mon = 'LY'
        else:
            self.mon = 'HOA'
        self.uutien = 0
        y = self.maXT[1:]
        if y == '1':
            self.uutien = 2.0
        elif y == '2':
            self.uutien = 1.5
        elif y == '3':
            self.uutien = 1.0
        else:
            self.uutien = 0.0
        self.tongdiem = self.diemTH * 2 + self.diemCM + self.uutien
        self.trangthai = None
        if self.tongdiem >= 18:
            self.trangthai = 'TRUNG TUYEN'
        else:
            self.trangthai = 'LOAI'
    
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+self.mon+' '+'{:.1f}'.format(self.tongdiem)+' '+self.trangthai

t = int(input())
list = []
for i in range(t):
    list.append(GiaoVien(i+1, input(), input(), float(input()), float(input())))

list.sort(key= lambda x : -x.tongdiem)
print(*list, sep='\n')

        

'''
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
'''
