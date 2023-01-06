# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de
# testo simples. O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas

from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar nova pessoa
        cabecalho('Novo Cadastro')
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
        sleep(2)

