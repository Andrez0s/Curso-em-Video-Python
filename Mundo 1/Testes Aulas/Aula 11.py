print('\033[37mOlá, Mundo!\033[m')
cores = {'Limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[033m',
         'pretoebranco': '\033[7;30m'}
a = 3
b = 5
print('Os valores são {}{}{} e {}{}{}'.format(cores['pretoebranco'], a, cores['Limpa'], cores['azul'], b, cores['Limpa']))
