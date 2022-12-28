# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista
# Caso o número já exista na lista, ele não será adicionado, No final serão exibidos todos os valores únicos
# digitados em ordem crescente

lista = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in lista:
        lista.append(numero)
        opcao = input('Deseja continuar? S/n ').lower()
        if opcao == 's':
            continue
        else:
            break
    else:
        print('Valor duplicado! insira um valor único: ')
        continue
lista.sort()
print(lista)
