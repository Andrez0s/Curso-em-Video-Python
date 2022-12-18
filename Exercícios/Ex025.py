# Leia o nome de uma pessoa e siga se ela tem Silva no nome
nome = input('Digite seu nome completo: ')
if nome.count('Silva') or nome.count('silva'):
    print('Você tem Silva no nome')
else:
    print('Você não tem Silva no nome')
