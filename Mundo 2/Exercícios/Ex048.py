# Calcule a soma de todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500

contador = 0
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        contador += 1
        soma += i
print(f'A soma dos {contador} numeros ímpares de 1 a 500 é {soma}')
