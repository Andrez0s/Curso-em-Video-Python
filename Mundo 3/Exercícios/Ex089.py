# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta, No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente

ficha = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? S/N ').lower()
    if resp == 'n':
        break
print('-' * 25)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno: (999 interrompe): '))
    if opc == 999:
        break
    elif opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
