import os
os.system('cls')

print("======== VOCÊ É OBRIGADO A VOTAR? ========")

idade = int(input("Informe a sua idade: "))

if idade < 18 or idade > 65:
    print("Você não é obrigado a votar.")
else:
    print("Você é obrigado a votar.")