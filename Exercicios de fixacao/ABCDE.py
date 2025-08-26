import os
os.system('cls')

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
    status = "aprovado"
elif media >= 7.5:
    conceito = "B"
    status = "aprovado"
elif media >= 6.0:
    conceito = "C"
    status = "aprovado"
elif media >= 4.0:
    conceito = "D"
    status = "reprovado"
else: 
    conceito = "E"
    status = "reprovado"

#print(f"\nConceito: {conceito}")
print(f"O aluno está {status} com nota {conceito}")