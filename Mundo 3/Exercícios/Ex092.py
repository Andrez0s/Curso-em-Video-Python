# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# Dicionário, se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e
# o salário, calcule e acrescete, além da idade, com quantos anos a pessoa vai se aposentar
# Considerar 35 anos de contribuição

import datetime

cadastro = {}

while True:
    cadastro['nome'] = input('Nome: ')
    ano_nascimento = int(input('Ano de nascimento: '))
    cadastro['idade'] = idade = datetime.date.today().year - ano_nascimento
    cadastro['ctps'] = int(input('CTPS (0 não tem): '))
    if cadastro['ctps'] == 0:
        print(f'Nome tem o valor {cadastro["nome"]}')
        print(f'Idade tem o valor {cadastro["idade"]}')
        print(f'CTPS tem o valor {cadastro["ctps"]}')
        break
    else:
        cadastro['contratação'] = int(input('Ano de contratação: '))
        cadastro['salário'] = float(input('Salário: '))
        print(f'Nome tem o valor {cadastro["nome"]}')
        print(f'Idade tem o valor {cadastro["idade"]}')
        print(f'CTPS tem o valor {cadastro["ctps"]}')
        print(f'''Ano de contratação tem o valor {cadastro['contratação']}
Salário tem o valor R${cadastro['salário']:.2f}
Aposentadoria tem o valor {cadastro['contratação'] - ano_nascimento + 35}
''')
        break
