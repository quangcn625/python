
class Time:
    def __init__(self, id, name, giovao, giora) -> None:
        self.id = id
        self.name = name 
        self.giovao = giovao
        self.giora = giora
        x1 = int(self.giovao[0:2])
        x2 = int(self.giovao[3:])
        x3 = int(self.giora[0:2])
        x4 = int(self.giora[3:])
        self.thoigian = (x3 - x1) * 60 + (x4 - x2)
    
    def thoigianchoi(self):
        return f"{self.thoigian // 60} gio {self.thoigian % 60} phut"
    
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+self.thoigianchoi()
    
t = int(input())
list = []
for __ in range(t):
    id = input()
    name = input()
    giovao = input()
    giora = input()
    list.append(Time(id, name, giovao, giora))

list.sort(key= lambda x : -x.thoigian)
print(*list, sep= '\n')


'''
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
'''
