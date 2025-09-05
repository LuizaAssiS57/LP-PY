import os 
os.system('cls')

print("""
  CÓDIGO      PRATO            VALOR
    1       Picanha          R$ 25,00
    2       Lasanha          R$ 20,00
    3       Strogonoff       R$ 18,00
    4       Bife Acebolado   R$ 15,00
    5       Pão com ovo      R$ 5,00
""")

codigo = int(input("Digite o código do prato: "))

match codigo:
    case 1:
        prato = "Picanha"
        valor = 25.0
    case 2:
        prato = "Lasanha"
        valor = 20.0
    case 3:
        prato = "Strogonoff"
        valor = 18.0
    case 4:
        prato = "Bife Acebolado"
        valor = 15.0
    case 5:
        prato = "Pão com ovo"
        valor = 5.0
    case _:
        print("O código não corresponde a um dos pratos disponiveis!")

print(f"PRATO: {prato} \nVALOR: R$ {valor}")