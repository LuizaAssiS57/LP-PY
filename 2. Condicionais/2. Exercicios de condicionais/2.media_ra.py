import os
os.system('cls')

pn = float(input("Informe a primeira nota: "))
sn = float(input("Informe a segunda nota: "))
tn = float(input("Informe a terceira nota: "))

media = (pn + sn + tn) / 3

if media >= 7:
    print(f"O aluno está aprovado :) {media}")
else:
    print(f"O aluno está reprovado :( {media}")