import math

class Point:
    def __init__(self, p) -> None:
        self.x = p[0]
        self.y = p[1]
    
    def distance(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))
    
class Triangle:
    def __init__(self, p1, p2, p3) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self) -> str:
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return "INVALID"
        else:
            return('{:.3f}'.format(a + b + c))
    
t = int(input())
list = []
i = 0
for __ in range(t):
    list += [float(x) for x in input().split()]
for __ in range(t):
    print(Triangle(Point(list[i:i+2]), Point(list[i+2:i+4]), Point(list[i+4:i+6])))
    i += 6
