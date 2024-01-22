
class SinhVien:
    def __init__(self, ma, name, lop) -> None:
        self.ma = ma
        self.name = name
        self.lop = lop


class DiemDanh:
    def __init__(self, id, diemdanh, SV) -> None:
        self.id = id
        self.diemdanh = diemdanh
        self.SV = SV
        self.diemchuyencan = 10
        for i in diemdanh:
            if i == 'm':
                self.diemchuyencan -= 1
            elif i == 'v':
                self.diemchuyencan -= 2
            else:
                continue
        if self.diemchuyencan < 0:
            self.diemchuyencan = 0
    
    def __str__(self) -> str:
        if self.diemchuyencan == 0:
            return self.id+' '+self.SV.name+' '+self.SV.lop+' '+str(self.diemchuyencan)+' '+'KDDK'
        return self.id+' '+self.SV.name+' '+self.SV.lop+' '+str(self.diemchuyencan)
    



t = int(input())
list1, list2= [], []

for i in range(t):
    ma = input()
    name = input()
    lop = input()
    list1.append(SinhVien(ma, name, lop))
for i in range(t):
    id, diemdanh = [x for x in input().split()]
    for x in list1:
        if id == x.ma:
            list2.append(DiemDanh(id, diemdanh, x))
            break

for i in list1:
    for j in list2:
        if i.ma == j.id:
            print(j)
            break


'''
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
'''
