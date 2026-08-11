##Exercicio 3
class bhaskara:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__ (self):
        return str(self.a) + "x^2 " ## continuar ax2 + bx + c
    def resolver(self):
        delta = (self.b ** 2) - (4 * self.a * self.c)
        if delta < 0:
            return "Não existem raízes reais"
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return f"Existe uma raiz real: {x}"
        else:
            x1 = (-self.b + delta ** 0.5) / (2 * self.a)
            x2 = (-self.b - delta ** 0.5) / (2 * self.a)
            return f"Existem duas raízes reais: {x1} e {x2}"

# Programa principal
input_a = float(input("Digite o valor de a: "))
input_b = float(input("Digite o valor de b: "))
input_c = float(input("Digite o valor de c: "))

equacao = bhaskara(input_a, input_b, input_c)
print(equacao.resolver())


