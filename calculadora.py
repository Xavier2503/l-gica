n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))

print("\nOperações: 1-Adição | 2-Subtração | 3-Multiplicação | 4-Divisão | 5-Potência | 6-Raiz quadrada | 7-Número par | 8-Número ímpar")
op = int(input("Escolha a operação: "))

if op == 1:
    print(f"Resultado: {n1 + n2}")
elif op == 2:
    print(f"Resultado: {n1 - n2}")
elif op == 3:
    print(f"Resultado: {n1 * n2}")
elif op == 4:
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Não é possível dividir por zero!")
elif op == 5:
    print(f"Resultado: {n1 ** n2}")
elif op == 6:
    print(f"Raiz quadrada do 1º: {n1 ** 0.5}")
    print(f"Raiz quadrada do 2º: {n2 ** 0.5}")
elif op == 7:
    print(f"O 1º número é par? {'Sim' if n1 % 2 == 0 else 'Não'}")
    print(f"O 2º número é par? {'Sim' if n2 % 2 == 0 else 'Não'}")
elif op == 8:
    print(f"O 1º número é ímpar? {'Sim' if n1 % 2 != 0 else 'Não'}")
    print(f"O 2º número é ímpar? {'Sim' if n2 % 2 != 0 else 'Não'}")
else:
    print("Operação inválida!")