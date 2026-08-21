# Sinalização - Exercício Aula 5
#

f = open("C:\\Repositorio\\puc-estudos\\websin.csv", encoding="utf-8")

for line in f:
    print(line.strip().split(";"))
f.close()
