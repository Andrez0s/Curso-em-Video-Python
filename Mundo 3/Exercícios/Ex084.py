# leia o nome e peso de várias pessoas, guardando tudo em uma lista, no final mostre: A > Quantas pessoas foram
# Cadastradas, B > Uma listagem com as pessoas mais pesadas, C > Uma listagem com as pessoas mais leves

pessoas = []
dados = []
maior_peso = 0
menor_peso = 0
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        elif dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = input('Deseja continuar? S/N ').strip().lower()
    if opcao == 'n':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {maior_peso}Kg peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'{p[0]}', end=',')
print(f'\nO menor peso foi {menor_peso}Kg peso de ', end=',')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'{p[0]}', end=',')
