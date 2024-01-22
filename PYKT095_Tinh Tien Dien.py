
class KhachHang:
    def __init__(self, stt, name, a) -> None:
        self.id = 'KH{:02d}'.format(stt)
        self.name = self.ChuanHoa(name)
        self.hoGD = a[0]
        self.csDau = int(a[1])
        self.csCuoi = int(a[2])
        sodien = self.csCuoi - self.csDau
        self.tientrongDM = 0
        if self.hoGD == 'A':
            if sodien < 100:
                self.tientrongDM = sodien * 450
            else:
                self.tientrongDM = 100 * 450
        elif self.hoGD == 'B':
            if sodien < 500:
                self.tientrongDM = sodien * 450
            else:
                self.tientrongDM = 500 * 450
        else:
            if sodien < 200:
                self.tientrongDM = sodien * 450
            else:
                self.tientrongDM = 200 * 450
        self.tienvuotDM = 0
        if self.hoGD == 'A':
            if sodien > 100:
                self.tienvuotDM = (sodien - 100) * 1000
            else:
                self.tienvuotDM = 0
        elif self.hoGD == 'B':
            if sodien > 500:
                self.tienvuotDM = (sodien - 500) * 1000
            else:
                self.tienvuotDM = 0
        else:
            if sodien > 200:
                self.tienvuotDM = (sodien - 200) * 1000
            else:
                self.tienvuotDM = 0
        self.thueVAT = self.tienvuotDM // 20
        self.tongtien = self.tientrongDM + self.tienvuotDM + self.thueVAT
    
    def ChuanHoa(self, s):
        s = s.strip().title()
        ans = ''
        for i in s.split():
            ans += i + ' '
        return ans.strip()

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.tientrongDM} {self.tienvuotDM} {self.thueVAT} {self.tongtien}"
    
a = []
for i in range(int(input())):
    a.append(KhachHang(i+1, input(), list(map(str, input().split()))))

a.sort(key= lambda x : (-x.tongtien))
print(*a, sep='\n')
        
# 2
#  nGuyEn Hong Ngat
# C 200 278
#  Chu thi    minh
# A 120 160