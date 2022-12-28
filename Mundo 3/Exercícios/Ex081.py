# Crie um programa que leia varios numeros e coloque em uma lista, depois disso mostre:
# A > Quantos números foram digitados, B > Lista de valores ordenada de forma decrescente
# C > Se o valor 5 foi digitado e está ou não na lista

lista = []
while True:
    numero = lista.append(int(input('Digite um numero')))
    opcao = input('Deseja continuar? S/N ').lower()
    if opcao == 'n':
        break
print(f'Foram digitados {len(lista)} Números')
lista.sort(reverse=True)
print(f'Os valores em ordem descrescente ficam: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)}')
else:
    print('O valor 5 não foi encontrado na lista')
