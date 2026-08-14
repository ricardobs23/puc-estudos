import math

"""
    >>> p = Point(3, 4)
    >>> p.x
    3
    
    >>> p = Point(3.0, 4.0)
    >>> p.y
    4.0

    >>> p1 = Point(3, 0)
    >>> p2 = Point(0, 4)
    >>> p1.distance(p2)
    5.0
"""

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