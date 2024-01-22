
class HoaDon:
    def __init__(self, id, name, soluong, dongia, tientrietkhau) -> None:
        self.id = id
        self.name = name
        self.soluong = soluong
        self.dongia = dongia
        self.tientrietkhau = tientrietkhau
        self.tongtien = self.soluong * self.dongia - self.tientrietkhau
    
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+str(self.soluong)+' '+str(self.dongia)+' '+str(self.tientrietkhau)+' '+str(self.tongtien)

list = []
for i in range(int(input())):
    list.append(HoaDon(input(), input(), int(input()), int(input()), int(input())))

list.sort(key= lambda x : -x.tongtien)
print(*list, sep='\n')
    

'''
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
'''