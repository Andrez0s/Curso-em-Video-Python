# Faça um mini sistema que utilize o interactive Help, o usuário vai digitar o comando e o manual vai aparecer
# quando o usuário digitar a palavra Fim, o programa se encerrará

def ajuda(com):
    help(com)


comando = ''
while True:
    comando = input('Função ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
