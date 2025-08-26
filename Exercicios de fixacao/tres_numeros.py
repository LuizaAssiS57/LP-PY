import os
os.system('cls')

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
numero3 = float(input("Informe o terceiro número: "))

maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print(f"\nEsses foram os números informados: {numero1}, {numero2}, {numero3}")
print(f"\nO maior número: {maior}")
print(f"\nO menor número: {menor}")