# Crie um programa para ler vários números e colocar em uma lista, depois crie 2 listas extras
# que vão conter apenas os valores pares e os valores ímpares digitados, mostre as 3 listas

lista_geral = []
lista_pares = []
lista_impares = []
while True:
    numero = lista_geral.append(int(input('Digite um número: ')))
    opcao = input('Deseja continuar? S/N ')
    if opcao == 'n':
        break
for item in lista_geral:
    if item % 2 == 0:
        lista_pares.append(item)
    else:
        lista_impares.append(item)
print(f'''A lista completa é {lista_geral}
A lista de pares é {lista_pares}
A lista de ímpares é {lista_impares}
''')
