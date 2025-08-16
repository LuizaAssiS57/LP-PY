import os

#FUNÇÃO PARA AUXILIAR LER AS NOTAS

def ler_nota(mensagem):
    while True:
        nota_str = input(mensagem)
        nota_str_corrigida = nota_str.replace(',', '.')
        try:
            nota_float = float(nota_str_corrigida)
            return nota_float
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número (ex: 8.8 ou 8,8).")

alunos_cadastrados = []

numero_alunos = 12

for i in range(numero_alunos):

    os.system('cls' if os.name == 'nt' else 'clear')

    #ENTRADA DE DADOS

    print("= INFORMAÇÕES DO ALUNO =")
    print(f"(Resgistrando aluno {i + 1} de {numero_alunos})")
    print("")

    nome_aluno = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    primeira_nota = ler_nota("Digite a primeira nota: ")
    segunda_nota = ler_nota("Digite a segunda nota: ")
    terceira_nota = ler_nota("Digite a terceira nota: ")
    quarta_nota = ler_nota("Digite a quarta nota: ")

    #PROCESSAMENTO DE DADOS

    soma = primeira_nota + segunda_nota + terceira_nota + quarta_nota
    media = soma / 4
    status = "APROVADO :)" if media >= 7 else "REPROVADO :("

    dados_aluno = {
        "nome": nome_aluno,
        "idade": idade,
        "notas": [primeira_nota, segunda_nota, terceira_nota, quarta_nota], 
        "media": media,
        "status": status
    }
    alunos_cadastrados.append(dados_aluno)

    #SAIDA DE DADOS

    print("\n= STATUS DO ALUNO =")
    print(f"\nAluno: {nome_aluno}")
    print(f"Idade: {idade}")
    print(f"A média do aluno é: {media:.1f} - Status: {status}")

    if i < 11:
        input("\nPressione Enter para cadastrar o próximo aluno...")
    else:
        input("\nPressione Enter para ver o relatório final...")

os.system('cls' if os.name == 'nt' else 'clear')
print("")
print("    RELATÓRIO FINAL DE ALUNOS")
print("")

for nome_aluno in alunos_cadastrados:
    print(f"\nNome: {nome_aluno['nome']}")
    print(f"Idade: {nome_aluno['idade']}")
    print(f"Notas: {nome_aluno['notas']}")
    print(f"Média Final: {nome_aluno['media']:.1f}")
    print(f"Status: {nome_aluno['status']}")
    print("-" * 25)

print("\nCadastro e relatório finalizados!")