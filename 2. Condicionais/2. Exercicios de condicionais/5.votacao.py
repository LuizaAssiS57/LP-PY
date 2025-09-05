import os
os.system('cls')

idade = float(input("Informe sua idade: "))

if idade < 16:
    print("Você não pode votar!")
elif idade in [16, 17]:
    print("Voto é opicional.")
elif 18 <= idade <= 64:
    print("Voto obrigatório.")
else:
    print("Voto não obrigatório.")
