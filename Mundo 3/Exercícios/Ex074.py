# Crie um programa que gere 5 números aleatórios e coloque em uma tupla, depois disso mostre a
# listagem de números gerados e também indique o menor e o maior valor que estão na tupla

# Com Biblioteca numpy
from numpy import random

tupla = tuple(random.randint(0, 11, size=5))  # Aleatorizando 5 números de 0 a 11
print(f'''{tupla}
O menor número é {min(tupla)}
O maior número é {max(tupla)}
''')

# Com Biblioteca random
#from random import randint
#tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
#print(f'''{tupla}
#O menor número é {min(tupla)}
#O maior número é {max(tupla)}
#''')
