# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro()
# e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções


def aumentar(preco=0, porcentagem=0, formatar=False):
    res = int(preco + preco * (porcentagem / 100))
    return res if formatar is False else moeda(res)


def diminuir(preco=0, porcentagem=0, formatar=False):
    res = int(preco - preco * (porcentagem / 100))
    return res if formatar is False else moeda(res)


def dobro(preco=0, formatar=False):
    res = int(preco * 2)
    return res if formatar is False else moeda(res)


def metade(preco=0, formatar=False):
    res = int(preco / 2)
    return res if formatar is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


# def moeda(variavel):
#    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
#    variavel = locale.currency(variavel)
#    return variavel
