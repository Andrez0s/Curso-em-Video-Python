# Leia 2 números inteiros e compáre-os, mostrando na tela uma mensagem:
# O primeiro valor é maior, O segundo valor é maior, Não existe valor maior, os dois são iguais

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
