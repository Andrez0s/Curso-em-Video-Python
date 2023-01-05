# Crie um programa que gerencie o aproveitamento de um jogador de futebol,o programa vai ler o nome
# e quantas partidas ele jogou, Depois vai ler a quantidade de gols feitos em cada partida. No final
# Tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

info = {}
partidas = []
info['nome'] = input('Nome do Jogador: ')
info['gols'] = lista = []
qtd_partidas = int(input(f'Quantas partidas {info["nome"]} jogou? '))
for i in range(0, qtd_partidas):
    partidas.append(int(input(f'Quantos gols na partida {i + 1}? ')))
info['gols'] = partidas[:]
info['total_gols'] = sum(partidas)
print(f'*=' * 20)
print(info)
print(f'*=' * 20)
for chave, valor in info.items():
    print(f'O campo {chave} tem o valor {valor}')
print(f'*=' * 20)
print(f'O jogador {info["nome"]} jogou {qtd_partidas} partidas.')
for item, valor in enumerate(info['gols']):
    print(f' - Na partida {item + 1}, fez {valor} gols')
print(f'Foi um total de {info["total_gols"]} gols')
