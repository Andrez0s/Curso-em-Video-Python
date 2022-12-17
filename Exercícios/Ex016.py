# Pegar o inteiro de um número para inteiro
from math import trunc
n = float(input('Insira um numero real: '))
# com biblioteca
print(f'A parte inteira do seu número é {trunc(n)}')

# Sem biblioteca
print(f'A parte inteira do seu número é {int(n)}')
