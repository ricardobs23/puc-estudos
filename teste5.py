import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

x1, y1 = [float(a) for a in input().split()]
x2, y2 = [float(a) for a in input().split()]
p1 = Point(x1, y1)
p2 = Point(x2, y2)
d = p1.distance(p2)
print(f"{d:.4f}")