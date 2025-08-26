import os
os.system('cls')

peso = float(input("Informe o seu peso: "))
altura = float(input("informe sua altura: "))

imc = peso / (altura ** 2)

if imc >= 40:
    classificacao = "Obesidade III (mórbida)"
elif imc >= 35:
    classificacao = "Obesidade II (severa)"
elif imc >= 30:
    classificacao = "Obesidade I"
elif imc >= 25:
    classificacao = "Levemente acima do peso"
elif imc >= 18:
    classificacao = "Peso ideal (parabéns)"
else:
    classificacao = "Abaixo do peso"

print(f"{classificacao}")
