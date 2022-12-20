# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import radians, degrees, sin, cos, tan
angulo = radians(float(input('Digite o angulo desejado : ')))
print(f'O angulo de {degrees(angulo):.2f} tem o seno de {sin(angulo):.2f}')
print(f'O angulo de {degrees(angulo):.2f} tem o cosseno de {cos(angulo):.2f}')
print(f'O angulo de {degrees(angulo):.2f} tem a tangente de {tan(angulo):.2f}')


