import math
class PS:
    def __init__(self, x, y) -> None:
        #Tim USC
        n = math.gcd(x, y)
        self.x = int(x/n)
        self.y = int(y/n)
    def __str__(self) -> str:
        return f'{self.x}/{self.y}'

tu, mau = [int(i) for i in input().split()]
print(PS(tu, mau))
    