# Leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade;
# até 9 anos: Mirim, de 10 a 14 anos: Infantil, de 15 até 19: Júnior, 20 anos: Sênior, 21 acima: Master

import datetime

ano_nascimento = int(input('Digite o ano de nascimento do aluno: '))
data = datetime.date.today()
ano = data.year
idade = ano - ano_nascimento
if idade <= 9:
    print(f'{idade} anos, Categoria: Mirim')
elif idade <= 14:
    print(f'{idade} anos, Categoria: Infantil')
elif idade <= 19:
    print(f'{idade} anos, Categoria: Júnior')
elif idade <= 25:
    print(f'{idade} anos, Categoria: Sênior')
else:
    print(f'{idade} anos, Categoria: Master')
