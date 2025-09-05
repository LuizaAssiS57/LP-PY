import os
os.system("cls")

num = int(input("Escolha um número de 1 até 12: "))

match num:
    case 1:
        mes = "Janeiro"
    case 2:
        mes = "Fevereiro"
    case 3:
        mes = "Março"
    case 4:
        mes = "Abril"
    case 5:
        mes = "Maio"
    case 6:
        mes = "Junho"
    case 7:
        mes = "Julho"
    case 8:
        mes = "Agosto"
    case 9:
        mes = "Setembro"
    case 10:
        mes = "Outubro"
    case 11:
        mes = "Novembro"
    case 12:
        mes = "Dezembro"

print(f"O número que você escolheu corresponde ao mês de {mes}.")
    