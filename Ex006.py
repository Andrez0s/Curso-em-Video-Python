print('===Calcular dobro, triplo e raiz quadrada de um número===')
n1 = int(input('Digite um número: '))
# primeira forma de fazer, salvando os valores em variáveis
#d = n1 * 2
#t = n1 * 3
#raiz = n1 ** 0.5

# ou diretamente na função print
# raiz quadrada pode ser feito com a função pow(n, 0.5)
print(f'O dobro de {n1} é {n1 * 2}')
print(f'O triplo de {n1} é {n1 * 3}')
print(f'A raiz quadrada de {n1} é {n1 ** 0.5:.2f}')

