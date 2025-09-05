import os
os.system('cls')

operador = input("Escolha um operador: (+, -, *, /) ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segunda número: "))

match operador:
    case "+":
        resultado = n1 + n2
        print(f"Os números escolhidos foram {n1} e {n2}.")
        print(f"O operador escolhido foi o +.")
        print(f"O resultado da operação foi: {resultado}")
    case "-":
        resultado = n1 - n2
        print(f"Os números escolhidos foram {n1} e {n2}.")
        print(f"O operador escolhido foi o -.")
        print(f"O resultado da operação foi: {resultado}")
    case "*":
        resultado = n1 * n2
        print(f"Os números escolhidos foram {n1} e {n2}.")
        print(f"O operador escolhido foi o *.")
        print(f"O resultado da operação foi: {resultado}")
    case "/":
        resultado = n1 / n2
        print(f"Os números escolhidos foram {n1} e {n2}.")
        print(f"O operador escolhido foi o /.")
        print(f"O resultado da operação foi: {resultado}")
    case _: 
        print("Operação inválida")


print("========== FIM =========")
