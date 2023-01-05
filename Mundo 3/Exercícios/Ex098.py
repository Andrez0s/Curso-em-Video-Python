# Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros: Início, fim e passo e
# Realize a contagem. Seu programa tem que realizar três contagens através da função criada:
# A > de 1 até 10, de 1 em 1    B > De 10 até 0, de 2 em 2    C > Uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('FIM')


contador(1, 10, 1)
print()
contador(10, -1, -2)
print()
print('Personalize sua contagem')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
