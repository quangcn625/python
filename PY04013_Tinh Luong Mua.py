import datetime

class LuongMua:
    def __init__(self, stt, name, timeStart, timeFinish, luongmua) -> None:
        self.id = 'T{:02d}'.format(stt)
        self.name = name
        self.timeStart = timeStart
        self.timeFinish = timeFinish
        self.luongmua = luongmua
        x = datetime.datetime.strptime(self.timeStart, '%H:%M')
        y = datetime.datetime.strptime(self.timeFinish, '%H:%M')
        self.thoigianmua = (y - x).seconds / 3600

    def Update(self, other):
        self.thoigianmua += other.thoigianmua
        self.luongmua += other.luongmua

    def result(self):
        return round(self.luongmua / self.thoigianmua, 2)
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {'{:.2f}'.format(self.result())}"

a = []
for i in range(int(input())):
    nametram = input()
    timeStart = input()
    timeFinish = input()
    luongmua = int(input())
    tmp = LuongMua(i+1, nametram, timeStart, timeFinish, luongmua)
    check = 1
    for j in a:
        if nametram == j.name:
            check = 0
            j.Update(tmp)
            break
    if check == 1:
        a.append(tmp)

print(*a, sep='\n')

# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35
    

    

        