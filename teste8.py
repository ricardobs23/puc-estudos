# Sinalização - Exercício Aula 5
#

f = open("C:\\Repositorio\\puc-estudos\\websin.csv", encoding="utf-8")

antiga = ""
for line in f:
    if antiga == "" or antiga < line.strip().split(";")[4]:
       antiga = line.strip().split(";")[4]
    print(line.strip().split(";"))

print(antiga)

f.close()

