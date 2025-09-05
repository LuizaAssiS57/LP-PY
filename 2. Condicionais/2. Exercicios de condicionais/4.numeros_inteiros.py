import os 
os.system('cls')

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um número inteiro: "))

soma = numero1 + numero2
produto = numero1 * numero2

maior = max(numero1, numero2)
menor = min(numero1, numero2)

print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

if numero1 == numero2:
    print("Os números são iguais!")