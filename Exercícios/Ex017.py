# Faça um programa que leia o comprimentodo cateto oposto e do cateto adjacente
# de um triângulo retângulo, Calcule e mostre o comprimento da hipotenusa.

from math import hypot
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
# Sem biblioteca
hipo = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** 0.5
print(f'O valor da Hipotenusa é: {hipo:.2f}')

# Com biblioteca
print(f'O valor da Hipotenusa é: {hypot(cateto_oposto, cateto_adjacente):.2f}')
