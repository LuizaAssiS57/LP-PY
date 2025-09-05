import os
os.system('cls')

while True:

    idnt_sx = input("Para masculino (M), Para feminino (F) ").strip().upper()
    altura = float(input("Informe a sua altura: "))

    match idnt_sx:
        case "M":
            ps_ideal = (72.7 * altura) - 58
        case "F":
            ps_ideal = (62.1 * altura) - 44.7
        case _:
            print("Inválido")

    print(f"O seu peso ideal é: {ps_ideal:.2f}")

    continuar = input("Deseja continuar? (s/n) ").lower()

    if continuar != "s":
        break

print("OBRIGADA")