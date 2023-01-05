# Faça um programa que leia nome e média de um aluni, guardando também a situação em um dicionário, no final
# mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = nome = input('Nome:')
aluno['media'] = media = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
if aluno["media"] < 7:
    print('Situação é igual a Reprovado')
else:
    print('Situação é Aprovado!')
