# Leia 2 valores e mostre um menu na tela com as opções de 1 > somar, 2 > multiplicar > 3 maior, > 4 > novos numeros,
# 5 sair

from time import sleep

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
opcao = '0'
while opcao != '5':
    opcao = input('''Escolha a opção de acordo com o que deseja realizar com os dois numero:'
    [1] - Soma
    [2] - Multiplicação
    [3] - Comparar qual número é maior
    [4] - Inserir novos números
    [5] - Sair do programa
    Sua Opção: ''')
    if opcao not in '12345':
        print('Opção inválida')
        print('-' * 30)
        continue
    if opcao == '1':
        print(f'A soma dos dois números é {numero1 + numero2}')
        print('-' * 30)
    elif opcao == '2':
        print(f'A multiplicação entre {numero1} e {numero2} é = {numero1 * numero2}')
        print('-' * 30)
    elif opcao == '3':
        if numero1 > numero2:
            print(f'O maior número é {numero1}')
            print('-' * 30)
        else:
            print(f'O maior número é {numero2}')
            print('-' * 30)
    elif opcao == '4':
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
    else:
        print('Finalizando Programa...')
        sleep(1)
        opcao = '5'
