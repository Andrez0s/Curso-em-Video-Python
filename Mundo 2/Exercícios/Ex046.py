# Mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0 com pausa de 1 segundo.

from time import sleep
from emoji import emojize

for i in range(10, -1, -1):
    print(i)
    sleep(0.5)
print(emojize('Feliz ano novo!:collision:'), end='')
print(emojize(':collision:' * 3))
