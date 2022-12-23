# Jogue par ou ímpar com o computador, o jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

rodadas = 0
venceu = True
while venceu:
    computador = randint(0, 10)
    valor_jogador = int(input('Digite um valor: '))
    par_impar_jogador = input('Par ou ímpar? P/I? ').lower()
    if par_impar_jogador == 'p':
        if (computador + valor_jogador) % 2 == 0:
            rodadas += 1
            print(f'Você VENCEU! o computador jogou {computador} e você jogou {valor_jogador} Resultando em Par')
        else:
            venceu = False
            print(f'Você perdeu! o computador jogou {computador} e você jogou {valor_jogador} Resultando em ímpar')
            break
    else:
        if (computador + valor_jogador) % 2 == 0:
            venceu = False
            print(f'Você perdeu! o computador jogou {computador} e você jogou {valor_jogador} Resultando em Par')
            break
        else:
            rodadas += 1
            print(f'Você VENCEU! o computador jogou {computador} e você jogou {valor_jogador} Resultando em ímpar')
print(f'Você ganhou {rodadas} vezes consecutivas')
