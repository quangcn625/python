
class ThuPhi:
    def __init__(self, bien, loaixe, soghe, huongdi, ngayDC) -> None:
        self.bien = bien
        self.loaixe = loaixe
        self.soghe = soghe
        self.huongdi = huongdi
        self.ngayDC = ngayDC


a, b = [], []
for i in range(int(input())):
    lst = list(map(str, input().split()))
    bien = lst[0]
    loaixe = lst[1]
    soghe = int(lst[2])
    huongdi = lst[3]
    ngayDC = lst[4]
    a.append(ThuPhi(bien, loaixe, soghe, huongdi, ngayDC))
    if ngayDC not in b:
        b.append(ngayDC)

for x in b:
    s = 0
    for y in a:
        if x == y.ngayDC:
            if y.huongdi == 'IN' and y.loaixe == 'Xe_con' and y.soghe == 5:
                s += 10000
            elif y.huongdi == 'IN' and y.loaixe == 'Xe_con' and y.soghe == 7:
                s += 15000
            elif y.huongdi == 'IN' and y.loaixe == 'Xe_tai' and y.soghe == 2:
                s += 20000
            elif y.huongdi == 'IN' and y.loaixe == 'Xe_khach' and y.soghe == 29:
                s += 50000
            elif y.huongdi == 'IN' and y.loaixe == 'Xe_khach' and y.soghe == 45:
                s += 70000
    print(x + ': ' + str(s))

# 5
# 29H-222.68 Xe_tai 2 IN 07/11/2021
# 30G-511.15 Xe_con 5 IN 07/11/2021
# 30F-123.15 Xe_con 5 OUT 06/11/2021
# 30F-123.15 Xe_con 5 IN 06/11/2021
# 30H-123.15 Xe_con 7 IN 06/11/2021

