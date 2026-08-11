## Exercício 1
class Employee:
    def __init__(self, name, setor,salary):
        self.name = name
        self.salary = salary
        self.setor = setor

    def __str__(self):
        return f'{self.name} recebe R$ {self.salary:.2f}'

    def proporcional(self,days):
        return self.salary / 30 * days

empregado = Employee('João', "TI", 7500)
print(empregado.name)
print(empregado.setor)
print(empregado.proporcional(1))