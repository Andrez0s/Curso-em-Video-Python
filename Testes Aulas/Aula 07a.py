# Ordem de precedência:

# 1° - Parênteses ()
# 2° - Exponenciação **
# 3° - * / // %
# 4° - + e -

# nome = input('Qual é seu nome?: ')
# print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {s},\no produto é {m},\na divisão é {d:.2f},', end='')
print(f'a divisão inteira é {di},\ne a exponenciação é {e}.')
