import datetime

class CaThi:
    def __init__(self, stt, ngaythi, giothi, phongthi):
        self.id = 'C{:03d}'.format(stt)
        self.ngaythi = ngaythi
        self.giothi = giothi
        self.phongthi = phongthi
    
    def __str__(self):
        return f"{self.id} {self.ngaythi} {self.giothi} {self.phongthi}"

f = open('CATHI.in', 'r')
t = int(next(f).strip())
a = []
for i in range(t):
    a.append(CaThi(i+1, next(f).strip(), next(f).strip(), next(f).strip()))

a.sort(key= lambda x : (datetime.datetime.strptime(x.ngaythi, '%d/%m/%Y'), datetime.datetime.strptime(x.giothi, '%H:%M'), x.id))
print(*a, sep='\n')

