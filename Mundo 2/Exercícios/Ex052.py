# leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
if total == 2:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo.')
