# leia o salário de um funcionário e calcule o valor do seu aumento para salários superiores a 1250 aumento de 10%
# para salários inferiores ou iguais aumento de 15%
salario = float(input('Digite o seu salário: '))
if salario > 1250:
    novo = (salario * 0.10) + salario
else:
    novo = (salario * 0.15) + salario
print(f'Seu novo salário será de {novo:.2f}')
