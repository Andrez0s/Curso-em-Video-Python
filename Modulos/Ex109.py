# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda()

from uteis import moeda


preco = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco, formatar=True))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco, formatar=True))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10, formatar=True))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(preco, 13, formatar=True))}')
