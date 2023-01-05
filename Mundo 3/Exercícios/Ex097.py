# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# E mostre uma mensagem com tamanho adaptável

def escreva(texto):
    print('~' * (len(texto) + 4))
    print(f'  {texto}')
    print('~' * (len(texto) + 4))


escreva('André')
escreva('Curso em video python')
