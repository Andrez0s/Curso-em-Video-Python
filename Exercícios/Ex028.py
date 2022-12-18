# Pense em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
from random import randint
from time import sleep
n = randint(0, 5)
print('Processando...')
sleep(1)
tentativa = int(input('Estou pensando em um número entre 0 e 5, tente adivinhar qual foi: '))
print('Calculando...')
sleep(2)
if tentativa == n:
    print(f'Parabéns você acertou! o número é {n}')
else:
    print('Você errou.')
