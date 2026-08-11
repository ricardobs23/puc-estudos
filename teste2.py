## Exercício 2
class calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def somar(self):
        return self.a + self.b
    def __str__(self):
        return str(a) + " + " + str(b) + " = " + str(self.somar())

    
# programa principal
a = int(input())
b = int(input())

calc = calculadora(a, b)

x = calc.somar()

print("X =", x)


ex1 = calculadora(10, 9)
ex1.somar() == 19

ex1 = calculadora(10, 9)
str(ex1) == "10 + 9 = 19"

