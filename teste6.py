class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            raise TypeError("Para comparar, o outro objeto deve ser um ponto.")

    def __str__(self):
        return f"Point({self.x:}, {self.y:})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)

"""""
p = Point(3, 4)
print(p == "teste!")

print(p is p2)
"""

try:
   p = Point(12,45)
   s = "hello"
   if p == s:
      print("IGUAIS!")
except TypeError:
   print("Ocorreu um erro durante a execucao!")
print("**Fim**")