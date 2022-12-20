# Leia o ano de nascimentod e um jovem e informe de acordo com sua idade: se ele ainda vai se alistar ao serviço militar
# se é a hora de se alistar, se já passou do tempo do alistamento, deve também mostrar o tempo que falta ou que passou
# do prazo

import datetime
data = datetime.date.today()
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano = data.year
if ano - ano_nascimento == 18:
    print('Você tem 18 anos e está na hora de se alistar')
elif ano - ano_nascimento < 18:
    print(f'Ainda faltam {18 - (ano - ano_nascimento)} anos para você se alistar')
else:
    print(f'Já se passaram {ano - ano_nascimento - 18} anos e você precisa se alistar imediatamente')
