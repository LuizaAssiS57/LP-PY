import os
os.system('cls')

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

maior = max(numero1, numero2)
menor = min(numero1, numero2)

if numero1 > numero2:
    print(f"Este é o maior número: {numero1}")
elif numero2 > numero1: 
    print(f"Este é o maior número: {numero2}")
else:
    print("Os números são iguais!")

if numero1 != numero2:
    print(f"\nO maior número: {maior}")
    print(f"O menor número: {menor}")