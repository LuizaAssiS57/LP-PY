import os
os.system('cls')

codigo = int(input("Iforme o seu código de funcionario: "))
ano_nascimento = int(input("Informe seu ano de nascimento: "))
tempo_trabalho = float(input("Informe seu tempo de contribuição: "))

idade = 2025 - ano_nascimento

if ano_nascimento >= 65 or tempo_trabalho >= 30:
    print(f"\nCódigo do funcionario: {codigo}")
    print(f"\nIdade do funcionario: {idade}")
    print(f"\nTempo de contribuição: {tempo_trabalho}")
    print("Requerer aposentadoria")
else:
    print(f"\nCódigo do funcionario: {codigo}")
    print(f"\nIdade do funcionario: {idade}")
    print(f"\nTempo de contribuição: {tempo_trabalho}")
    print("Não requerer aposentadoria")
