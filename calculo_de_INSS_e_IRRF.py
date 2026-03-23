salario_bruto = float(input("Digite o valor do salário bruto: R$ "))

# Cálculo simplificado do INSS (Tabela de 2023 como base de estudos)
if salario_bruto <= 1302.00:
    inss = salario_bruto * 0.075
elif salario_bruto <= 2571.29:
    inss = salario_bruto * 0.09 - 19.53
elif salario_bruto <= 3856.94:
    inss = salario_bruto * 0.12 - 96.67
elif salario_bruto <= 7507.49:
    inss = salario_bruto * 0.14 - 173.80
else:
    inss = 876.95 # Teto do INSS

salario_base_irrf = salario_bruto - inss

# Cálculo do IRRF (Tabela de 2023 base)
if salario_base_irrf <= 1903.98:
    irrf = 0
elif salario_base_irrf <= 2826.65:
    irrf = (salario_base_irrf * 0.075) - 142.80
elif salario_base_irrf <= 3751.05:
    irrf = (salario_base_irrf * 0.15) - 354.80
elif salario_base_irrf <= 4664.68:
    irrf = (salario_base_irrf * 0.225) - 636.13
else:
    irrf = (salario_base_irrf * 0.275) - 869.36

print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Salário Líquido: R$ {(salario_bruto - inss - irrf):.2f}")