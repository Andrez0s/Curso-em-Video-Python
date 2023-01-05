# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep


def maior(*numero):
    if len(numero) > 0:
        print(f'Os números informados foram:', end=' ')
        for num in numero:
            print(num, end=' ')
            sleep(1)
        print(f'\nForam informados {len(numero)} valores ao todo')
        print(f'O maior número foi {max(numero)}')
        print('~' * 40)
    else:
        print(f'Não foi informado nenhum valor')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
