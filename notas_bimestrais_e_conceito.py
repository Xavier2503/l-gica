n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 9.0:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6.0:
    conceito = "C"
elif media >= 4.0:
    conceito = "D"
else:
    conceito = "E"

print(f"\nNotas do aluno: {n1}, {n2}, {n3}, {n4}")
print(f"Média Final: {media:.2f}")
print(f"Conceito: {conceito}")

if conceito in ["A", "B", "C"]:
    print("Resultado: APROVADO")
elif conceito in ["D", "E"]:
    print("Resultado: REPROVADO")