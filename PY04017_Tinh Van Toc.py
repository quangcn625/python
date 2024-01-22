import datetime

class VanToc:
    def __init__(self, name, donvi, thoidiemden) -> None:
        self.name = name
        self.donvi = donvi
        self.thoidiemden = thoidiemden
        # a = [i[0] for i in name.split()]
        # b = [i[0] for i in donvi.split()]
        # self.id = ''.join(b) + ''.join(a)
        ans = ''
        for i in donvi.split():
            ans += i[0:1]
        for i in name.split():
            ans += i[0:1]
        self.id = ans
    
    def thoigian(self):
        #CÁCH TÍNH GIỜ THỨ 1:
        # x = datetime.datetime.strptime('6:00', '%H:%M')
        # y = datetime.datetime.strptime(self.thoidiemden, '%H:%M')
        # return (y - x).seconds / 3600

        #CÁCH IN RA THEO GIỜ VÀ PHÚT:
        # self.time = y - x
        # self.time = str(self.time)
        # a = [int(i) for i in self.time.split(':')]
        # return '{} gio {} phut'.format(a[0], a[1])

        #CÁCH TÍNH GIỜ THỨ 2:
        x = '6:00'
        tmp1 = int(x[0:1])
        tmp2 = int(self.thoidiemden[0:1])
        tmp3 = int(x[2:len(x)])
        tmp4 = int(self.thoidiemden[2:len(self.thoidiemden)])
        return (tmp2 - tmp1) + (tmp4 - tmp3) / 60
    
    def vantoc(self):
        return 120 / self.thoigian()
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.donvi} {round(self.vantoc())} Km/h"
    
t = int(input())
list = []
for i in range(t):
    name = input()
    donvi = input()
    thoidiemden = input()
    list.append(VanToc(name, donvi, thoidiemden))

list.sort(key= lambda x : x.vantoc(), reverse=True)

for i in list:
    print(i)        


# 3
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45 