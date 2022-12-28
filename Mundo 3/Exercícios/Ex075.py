# Leia 4 valores pelo teclado e guarde-os em uma tupla, no final mostre: A > Quantas vezes apareceu
# O valor 9, B > Em que posição foi digitado o primeiro valor 3, C > Quais foram os números pares

numero = (int(input('Digite o primeiro número: ')),
          int(input('Digite o primeiro número: ')),
          int(input('Digite o primeiro número: ')),
          int(input('Digite o primeiro número: '))
          )

print(f'O número 9 apareceu {numero.count(9)} Vezes')
if 3 in numero:
    print(f'O valor 3 apareceu na posição {numero.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares foram', end='')
for item in numero:
    if item % 2 == 0:
        print(item, end=' ')
