# Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistemas de visualização
# de detalhes do aproveitamento de cada jogador

jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do Jogador: ')
    jogador['gols'] = lista = []
    qtd_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for i in range(0, qtd_partidas):
        partidas.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total_gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer Continuar? S/N ').upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{str(k):>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO Não existe jogador com o ncódigo {busca}')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('Volte Sempre!')
