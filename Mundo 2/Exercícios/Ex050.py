# Leia 6 números inteiros e mostre a soma apenas daqueles que forem pares, se for ímpar desconsidere-o

soma = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}° número: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares digitados é {soma}')
