# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
# jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente


def ficha(nome_jogador='<desconhecido>', gols_jogador=0):
    print(f'O jogador {nome_jogador} fez {gols_jogador} gols no campeonato')


nome = input('Nome do jogador: ')
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols_jogador=gols)
else:
    ficha(nome, gols)
