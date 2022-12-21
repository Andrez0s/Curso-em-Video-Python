# Leia o ano de nascimento de 7 pessoas, no final mostre quantas pessoas ainda não atingiram a maioridade e quantas
# ja são maiores

from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for pessoa in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {pessoa}° pessoa: '))
    if ano_atual - ano_nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Das 7 pessoas {maiores} são maiores e {menores} são menores')
