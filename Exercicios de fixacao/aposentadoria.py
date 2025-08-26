import os
os.system('cls')

codigo = int(input("Iforme o seu código de funcionario: "))
ano_nascimento = int(input("Informe seu ano de nascimento: "))
tempo_trabalho = float(input("Informe seu tempo de contribuição: "))

ano_agora = 2025
idade = ano_agora - ano_nascimento

if ano_nascimento >= 65 and tempo_trabalho >= 30:
    status = "Requerer aposentadoria"
else:
    status = "Não requerer aposentadoria"

print(f"\nCódigo do funcionario: {codigo}")
print(f"\nIdade do funcionario: {idade}")
print(f"\nTempo de contribuição: {tempo_trabalho}")
print(f"{status}")