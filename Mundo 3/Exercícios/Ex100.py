# Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar()
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores PARES sorteados pela função anterior

from numpy import random
from time import sleep

numeros = random.randint(low=0, high=10, size=5)


def sorteia():
    global numeros
    print(f'Os números sorteados foram: ', end='')
    for valor in numeros:
        print(valor, end=' ')
        sleep(0.5)


def somapar():
    global numeros
    soma = 0
    for item in numeros:
        if item % 2 == 0:
            soma += item
    print(f'\nA soma dos valores pares de {numeros} é {soma}')


sorteia()
somapar()
