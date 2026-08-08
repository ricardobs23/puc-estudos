class Employee:
    def __init__(self, name, setor,salary):
        self.name = name
        self.salary = salary
        self.setor = setor

    def __str__(self):
        return f'{self.name} recebe R$ {self.salary:.2f}'

    def proporcional(self,days):
        return self.salary / 30 * days

joao = Employee('João', "TI", 3000)
print(joao.name)
print(joao.setor)
print(joao.proporcional(1))
