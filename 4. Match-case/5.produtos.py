import os
os.system('cls')

while True:

    print("FINALIZANDO SUA COMPRA")

    vlr_produto = float(input("Informe o valor do produto: "))
    frm_pagamento = int(input("Informe a forma de pagamento: (1 para pagamento à vista ou 2 para pagamento à prazo) "))

    match frm_pagamento:
        case 1:
            desconto = vlr_produto * 0.10
            vlr_total = vlr_produto - desconto

            print("RECIBO")
            print(f"Valor do produto: R${vlr_produto:.2f}")
            print(f"Forma de pagamento: {frm_pagamento}- À vista")
            print(f"Valor do desconto: R${desconto:.2f}")
            print(f"Total a pagar: {vlr_total:.2f}")
        case 2:
            parcelas = int(input("Quantas parcelas: (Até 6x) "))
            
            print("RECIBO")
            print(f"Valor do produto: R${vlr_produto:.2f}")
            print(f"Forma de pagamento: {frm_pagamento}- À prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: R${vlr_produto/parcelas:.2f}")
            print(f"Total à prazo: R${vlr_produto:.2f}")
        case _:
            print("Forma de pagameto inválida")

    continuar = input("\nDeseja fazer outra compra? (s/n) ").strip().lower()

    if continuar != "s":
        break

print("OBRIGADA :)")