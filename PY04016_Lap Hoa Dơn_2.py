import datetime

class HoaDon:
    def __init__(self, stt, name, sophong, ngaynhanphong, ngaytraphong, dichvuphatsinh) -> None:
        self.id = 'KH{0:0>2}'.format(stt)
        self.name = name
        self.sophong = sophong
        self.ngaynhanphong = ngaynhanphong
        self.ngaytraphong = ngaytraphong
        self.dichvuphatsinh = dichvuphatsinh

    def songayo(self):
        songay = datetime.datetime.strptime(self.ngaytraphong, '%d/%m/%Y') - datetime.datetime.strptime(self.ngaynhanphong, '%d/%m/%Y')
        return songay.days + 1

    def thanhtien(self):
        x = self.sophong[0:1]
        if x == '1':
            return self.songayo() * 25 + self.dichvuphatsinh
        elif x == '2':
            return self.songayo() * 34 + self.dichvuphatsinh
        elif x == '3':
            return self.songayo() * 50 + self.dichvuphatsinh
        else:
            return self.songayo() * 80 + self.dichvuphatsinh
        
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+self.sophong+' '+str(self.songayo())+' '+str(self.thanhtien())
    
t = int(input())
list = []
for i in range(t):
    name = input().strip()
    sophong = input().strip()
    ngaynhanphong = input().strip()
    ngaytraphong = input().strip()
    dichvuphatsinh = int(input().strip())
    list.append(HoaDon(i+1, name, sophong, ngaynhanphong, ngaytraphong, dichvuphatsinh))

list.sort(key= lambda x : -x.thanhtien())
for i in list:
    print(i)

'''
3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96
'''
 