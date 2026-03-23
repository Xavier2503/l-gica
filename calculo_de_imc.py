peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")

if imc < 16:
    print("Classificação: Magreza grave")
elif imc < 17:
    print("Classificação: Magreza moderada")
elif imc < 18.5:
    print("Classificação: Magreza leve")
elif imc < 25:
    print("Classificação: Saudável")
elif imc < 30:
    print("Classificação: Sobrepeso")
elif imc < 35:
    print("Classificação: Obesidade Grau I")
elif imc < 40:
    print("Classificação: Obesidade Grau II (severa)")
else:
    print("Classificação: Obesidade Grau III (mórbida)")
