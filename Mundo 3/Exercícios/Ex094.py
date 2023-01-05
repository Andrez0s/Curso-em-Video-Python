# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoas em um
# Dicionário e todos os dicionários em uma lista. No final, mostre: A > Quantas pessoas foram cadastradas
# B > Média de idade, C > Uma lista com as mulheres, D > Uma lista de pessoas com idade acima da média

galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: M/F ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? S/N ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A média de idade é de {media:.2f} anos')
print('As mulheres cadastradas foram ', end='')
for pessoa in galera:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for pessoa in galera:
    if pessoa['idade'] >= media:
        print('   ')
        for key, value in pessoa.items():
            print(f'{key} = {value}; ', end='')
        print('')
print('Encerrado')
