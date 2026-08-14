class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, c):
        self.c = c
    def area(self):
        return 3.14159 * self.c * self.c

######

class Triangle(Shape):
    def __init__(self, a, c):
        self.a = a
        self.c = c
    def area(self):
        return (self.a * self.c) / 2

########

class Trapezoid(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        return ((self.a + self.b) * self.c) / 2

####

class Square(Shape):
    def __init__(self, b):
        self.b = b
    def area(self):
        return self.b * self.b

#########

class Rectangle(Shape):
    def __init__(self, a ,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

# Programa Principal
a, b, c = [float(x) for x in input().split()]

tri = Triangle(a, c)
print(f"Triangulo={tri.area():.3f}")

cir = Circle(c)
print(f"Circulo={cir.area():.3f}")

trap = Trapezoid(a, b, c)
print(f"Trapezio={trap.area():.3f}")

squ = Square(b)
print(f"Quadrado={squ.area():.3f}")

rec = Rectangle(a, b)
print(f"Retangulo={rec.area():.3f}")

