# Sortear entre 4 alunos quem vai apagar o quadro
from random import choice

lista = [input('Nome do aluno:'), input('Nome do aluno:'), input('Nome do aluno:'), input('Nome do aluno:')]
aluno = choice(lista)
print(f'O aluno que irá apagar o quadro será o {aluno}')
