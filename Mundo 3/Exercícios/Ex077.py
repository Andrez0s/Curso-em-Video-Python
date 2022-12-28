# Crie um programa que tenha uma tupla com várias palavras (não usar acentos) depois, você deve mostrar
# para cada palavra, quais são as suas vogais

palavras = ('lapis', 'homem', 'andre', 'kelen', 'festa', 'frango')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        # print(letra)
        if letra.lower() in 'aeiou':
            print(letra, end=',')
