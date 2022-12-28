# Leia 5 valores numéricos e guarde-os em uma lista, no final mostre qual foi o maior e o menor valor digitado,
# E suas respectivas posições na lista

valores = []
for item in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {item}: ')))
print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')
for i, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{i}...', end='')
