# Leia o nome completo de uma pessoa e mostre:
nome = input('Digite seu nome completo: ').strip()
# Nome com todas as letras maiúsculas
print(nome.upper())
# Nome com todas as letras minúsculas
print(nome.lower())
# Quantas letras no total sem considerar espaços
print('Seu nome contêm', len(nome) - nome.count(' '), 'letras')
# Quantas letras tem o primeiro nome
print('Seu primeiro nome tem', nome.find(' '), 'letras')
