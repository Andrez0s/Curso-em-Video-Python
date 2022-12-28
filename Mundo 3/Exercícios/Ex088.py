# Faça um programa que crie palpites para a Mega Sena, o programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

jogos = int(input('Quantos jogos você quer sortear? '))
lista = []
print(f'Sorteando {jogos} Jogos...')
for item in range(0, jogos):
    for jogo in range(0, 6):
        num_aleatorio = randint(1, 60)
        if num_aleatorio not in lista:
            lista.append(num_aleatorio)
    sleep(1)
    lista.sort()
    print(f'Jogo {item + 1}: {lista}')
    lista.clear()
print(f'Boa Sorte!')
