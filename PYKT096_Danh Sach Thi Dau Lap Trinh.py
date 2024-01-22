
class Team:
    def __init__(self, stt, tenTeam, tenTruong) -> None:
        self.idTeam = 'Team{:02d}'.format(stt)
        self.tenTeam = tenTeam
        self.tenTruong = tenTruong

class SinhVien:
    def __init__(self, stt, name, maTeam, tmp) -> None:
        self.maTS = 'C{:03d}'.format(stt)
        self.name = name
        self.maTeam = maTeam
        self.tmp = tmp
    
    def __str__(self) -> str:
        return f"{self.maTS} {self.name} {self.tmp.tenTeam} {self.tmp.tenTruong}"

a, b = [], []
for i in range(int(input())):
    a.append(Team(i+1, input(), input()))

for i in range(int(input())):
    name = input()
    maTeam = input()
    for j in a:
        if maTeam == j.idTeam:
            b.append(SinhVien(i+1, name, maTeam, j))
            break
    
b.sort(key= lambda x : x.name)
print(*b, sep='\n')

# 2
# BAV_MIS
# Banking Academy of Vietnam
# FTU Knights1
# Foreign Trade University
# 6
# Le Trung Toan
# Team01
# Nguyen Trinh Quoc Long
# Team01
# Giang Minh Tung
# Team01
# Nguyen Hang Giang
# Team02
# Nguyen Thanh Nhan
# Team02
# Nguyen Viet Duc
# Team02