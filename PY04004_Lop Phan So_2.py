import math

class PhanSo:
    def __init__(self, tu, mau) -> None:
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        n = math.gcd(self.tu, self.mau)
        x = PhanSo(1,1)
        x.tu = int(self.tu / n)
        x.mau = int(self.mau / n)
        return x
    
    def tinhtong(self, other):
        return PhanSo(other.tu * self.mau + other.mau * self.tu, other.mau * self.mau)

x, y, z, t = [int(i) for i in input().split()]
a = PhanSo(x, y)
b = PhanSo(z, t)
c = a.tinhtong(b)
c = c.rutgon()
print(f'{c.tu}/{c.mau}')