# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto Negado, Opcional(65) ou obrigatório


def voto(nascimento):
    from datetime import datetime
    idade = datetime.today().year - nascimento
    if idade < 16:
        return f'com {idade} anos: NÃO VOTA.'
    elif idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


ano_nascimento = int(input('Digite o ano de nascimento: '))
print(voto(ano_nascimento))
