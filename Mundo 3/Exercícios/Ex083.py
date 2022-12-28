# Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses,
# seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
# na ordem correta

expressao = input('Digite a expressão matemática: ')
lista = []
for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
