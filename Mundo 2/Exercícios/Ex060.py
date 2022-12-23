# Leia um número qualquer e mostre o seu fatorial

numero = int(input('Digite um número: '))
contagem = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while contagem > 0:
    print(f'{contagem} ', end='')
    print(' X ' if contagem > 1 else ' = ', end='')
    fatorial *= contagem
    contagem -= 1
print(fatorial)
