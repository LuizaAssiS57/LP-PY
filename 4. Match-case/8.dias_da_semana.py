import os
os.system('cls')

dia = int(input("Escolha um dia da semana: "))

match dia:
    case 1:
        tipo = "final de semana"
    case 2:
        tipo = "dia útil"
    case 3:
        tipo = "dia útil"
    case 4:
        tipo = "dia útil"
    case 5:
        tipo = "dia útil"
    case 6:
        tipo = "dia útil"
    case 7:
        tipo = "final de semana"
    case _:
        tipo = "dia inválido"

print(f"O dia que você escolheu é um {tipo}.")