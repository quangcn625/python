import datetime

class MonThi:
    def __init__(self, mamon, tenmon, hinhthucthi) -> None:
        self.mamon = mamon
        self.tenmon = tenmon
        self.hinhthucthi = hinhthucthi
    
class CaThi:
    def __init__(self, stt, ngaythi, giothi, idPhongThi) -> None:
        self.id = 'C{:03d}'.format(stt)
        self.ngaythi = ngaythi
        self.giothi = giothi
        self.idPhongThi = idPhongThi

class LichThi:
    def __init__(self, macathi, mamon, manhom, sosinhvien, tmp1, tmp2):
        self.macathi = macathi
        self.mamon = mamon
        self.manhom = manhom
        self.sosinhvien = sosinhvien
        self.tmp1 = tmp1
        self.tmp2 = tmp2
    
    def __str__(self):
        return f"{self.tmp2.ngaythi} {self.tmp2.giothi} {self.tmp2.idPhongThi} {self.tmp1.tenmon} {self.manhom} {self.sosinhvien}"

a, b, c = [], [], []

f1 = open('MONTHI.in', 'r')
t1 = int(next(f1).strip())
for i in range(t1):
    mamon = next(f1).strip()
    tenmon = next(f1).strip()
    hinhthucthi = next(f1).strip()
    a.append(MonThi(mamon, tenmon, hinhthucthi))

f2 = open('CATHI.in', 'r')
t2 = int(next(f2).strip())
for i in range(t2):
    ngaythi = next(f2).strip()
    giothi = next(f2).strip()
    phongthi = next(f2).strip()
    b.append(CaThi(i+1, ngaythi, giothi, phongthi))

f3 = open('LICHTHI.in', 'r')
t3 = int(next(f3).strip())
for i in range(t3):
    tmp = next(f3).strip().split()
    macathi = tmp[0]
    mamon = tmp[1]
    manhom = tmp[2]
    sosinhvien = tmp[3]
    tmp1 = None
    tmp2 = None
    for j in a:
        if mamon == j.mamon:
            tmp1 = j
            break
    for j in b:
        if macathi == j.id:
            tmp2 = j
            break
    c.append(LichThi(macathi, mamon, manhom, sosinhvien, tmp1, tmp2))

c.sort(key= lambda x : (datetime.datetime.strptime(x.tmp2.ngaythi, '%d/%m/%Y'), datetime.datetime.strptime(x.tmp2.giothi, '%H:%M'), x.macathi))

print(*c, sep='\n')
