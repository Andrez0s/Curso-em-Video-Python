# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {largura}x{comprimento} é de {a}M²')


print('Controle de Terrenos')
print('---------------------')
largura = float(input('Largura M: '))
comprimento = float(input('Comprimento M: '))
area(largura, comprimento)
