# Leia um número inteiro qualquer e peça par ao usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal 3 para hexadecimal

# Solicitando informações para usuário
numero = input('Digite o número a ser convertido: ')
opcao_escolhida = input('''
1 - para binário
2 - para octal
3 - para hexadecimal
Escolha uma das opções acima para converter seu número: ''')

if numero.isnumeric() and opcao_escolhida.isnumeric():  # Verificando se o que foi digitado é um número
    if opcao_escolhida == '1':
        print(format(int(numero), "b"))
    elif opcao_escolhida == '2':
        print(format(int(numero), "o"))
    elif opcao_escolhida == '3':
        print(format(int(numero), "x"))
    else:
        print('Opção inválida')  # Else para caso o que foi digitado não esteja dentro das opções de 1 a 3
else:
    print('Opção inválida')  # Else para caso o que foi digitado não seja número
