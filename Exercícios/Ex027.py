# Leia o nome completo de uma pesso, mostre o primeiro e o último nome separadamente.
nome = input('Digite seu nome completo: ').strip()
nome = nome.title().split()
print('Seu primeiro nome é:', nome[0])
print('Seu último nome é:', nome[-1])
