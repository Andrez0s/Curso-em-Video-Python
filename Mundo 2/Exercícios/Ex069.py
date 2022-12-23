# Leia a idade e o sexo de várias pessoas, a cada pessoa cadastrada o programa deverá perguntar se
# o usuário quer ou não continuar, no final mostre:
# A > Quantas pessoas tem mais de 18 anos
# B > Quantos homens foram cadastrados, C > Quantas mulheres tem menos de 20 anos.

pessoas_maior_18anos = 0
homens = 0
mulheres_menor_20anos = 0
total_cadastrados = 0
while True:
    total_cadastrados += 1
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa M/F:  ').lower()
    while sexo not in 'mf':
        sexo = input('Digite o sexo da pessoa M/F:  ').lower()
    if idade >= 18:
        pessoas_maior_18anos += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres_menor_20anos += 1
    opcao = input('Deseja continuar? S/N: ')
    if opcao == 'n':
        break
print('-'*35)
print(f'''Foram cadastradas no total {total_cadastrados} pessoas
{pessoas_maior_18anos} pessoas com mais de 18 anos
{homens} são homens
{mulheres_menor_20anos} são mulheres com menos de 20 anos
''')
