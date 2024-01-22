
class SoPhuc:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def tinhtong(self, other):
        return SoPhuc(other.x + self.x, other.y + self.y)
    
    def phepnhan(self, other):
        ans = SoPhuc(1,1)
        ans.x = other.x * self.x - other.y * self.y
        ans.y = other.x * self.y + other.y * self.x
        return ans
    
    def __str__(self):
        if self.y < 0:
            return f"{self.x} - {-self.y}i"
        else:
            return f"{self.x} + {self.y}i"

t = int(input())
for __ in range(t):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    a = SoPhuc(x1, y1)
    b = SoPhuc(x2, y2)
    c = a.tinhtong(b)
    print(str(c.phepnhan(a)) + ", " + str(c.phepnhan(c)))