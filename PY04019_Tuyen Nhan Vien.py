
class NhanVien:
    def __init__(self, id, name, score1, score2) -> None:
        self.name = name
        self.id = 'TS0' + str(id)
        while score1 > 10:
            score1 /= 10
        while score2 > 10:
            score2 /= 10
        self.score = (score1 + score2) / 2
    
    def getStatus(self):
        if (self.score < 5) :   return 'TRUOT'
        if (self.score < 8) :   return 'CAN NHAC'
        if (self.score <= 9.5) :   return 'DAT'
        else:   return "XUAT SAC"
    
    def __str__(self) -> str:
        return self.id+' '+self.name+' '+'{:.2f}'.format(self.score)+' '+self.getStatus()
    
t = int(input())
list = []
for i in range(t):
    name = input()
    lythuyet = float(input())
    thuchanh = float(input())
    list.append(NhanVien(i+1, name, lythuyet, thuchanh))

list.sort(key= lambda x : -x.score)
print(*list, sep='\n')

'''
12
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
'''
        