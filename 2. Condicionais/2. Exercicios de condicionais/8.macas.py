import os
os.system('cls')

quant_maca = int(input("Quantas maçãs deseja comprar? "))

if quant_maca >= 12: 
    print(f"Você comprou {quant_maca}.")
    valor_total = quant_maca * 1.00
else:
    print(f"Você comprou {quant_maca}.")
    valor_total = quant_maca * 1.30

print(f"\nO valor total da sua compra é: R$ {valor_total:.2f}")