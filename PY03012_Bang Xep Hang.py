
class SinhVien:
    def __init__(self, name, a) -> None:
        self.name = name
        self.lamdung = a[0]
        self.submit = a[1]
    
    def __str__(self) -> str:
        return self.name+' '+str(self.lamdung)+' '+str(self.submit)

t = int(input())
a = []
for __ in range(t):
    a.append(SinhVien(input(), list(map(int, input().split()))))

a.sort(key= lambda x : (-x.lamdung, x.submit, x.name))
print(*a, sep='\n')

# 5
# Nguyen Van Nam
# 168 600
# Tran Thi Ngoc
# 168 600
# Le Gia Quang
# 168 500
# Nguyen Truong An
# 168 600
# Bui Truong Son
# 170 300