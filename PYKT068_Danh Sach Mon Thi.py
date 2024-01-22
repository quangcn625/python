
class MonThi:
    def __init__(self, id, name, hinhthucthi) -> None:
        self.id = id
        self.name = name
        self.hinhthucthi = hinhthucthi

    def __str__(self) -> str:
        return '{} {} {}'.format(self.id, self.name, self.hinhthucthi)

List = []
for i in range(int(input())):
    List.append(MonThi(input(), input(), input()))

List.sort(key= lambda x : (x.id))
print(*List, sep='\n')

# 2
# MUL1320
# Nhap mon da phuong tien
# Bai tap lon + Van dap truc tuyen
# BAS1203
# Giai tich 1
# Thi viet + Van dap truc tuyen