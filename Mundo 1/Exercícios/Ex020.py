# Definir a ordem de apresentação de um trabalho entre 4 alunos

from random import shuffle

lista = [input('Digite o nome do aluno: '), input('Digite o nome do aluno: '), input('Digite o nome do aluno: '),
         input('Digite o nome do aluno: ')]
shuffle(lista)
print(f'A ordem de apresentação será: {lista}')
