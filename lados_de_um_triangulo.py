a = float(input("Digite o 1º lado do triângulo: "))
b = float(input("Digite o 2º lado do triângulo: "))
c = float(input("Digite o 3º lado do triângulo: "))

# Condição de existência de um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os valores podem formar um triângulo.")
    if a == b == c:
        print("Tipo: Triângulo Equilátero")
    elif a != b and a != c and b != c:
        print("Tipo: Triângulo Escaleno")
    else:
        print("Tipo: Triângulo Isósceles")
else:
    print("Os valores NÃO formam um triângulo.")