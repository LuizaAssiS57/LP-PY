import os 
os.system('cls')

print("======= LOGIN =======")

email = input("Email: ")
senha = str(input("Senha: "))

if email == "admin@.com" and senha == "12345":
    print("Bem-vindo!")
else:
    print("Login ou senha inválidos.")