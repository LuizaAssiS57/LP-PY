import os
os.system('cls')

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = n1 + n2
produto = n1 * n2

maior = max(n1, n2)
menor = min(n1, n2)

print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")