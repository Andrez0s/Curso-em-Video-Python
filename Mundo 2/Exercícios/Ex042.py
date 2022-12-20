# Refaça o exercício 35 e acrescente o tipo de triângulo que será formado: Equilátero: Todos os lados iguais,
# Isósceles: dois lados iguais, Escaleno: todos os lados diferentes


r1 = float(input('Insira o comprimento da reta 1: '))
r2 = float(input('Insira o comprimento da reta 2: '))
r3 = float(input('Insira o comprimento da reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  # Verificando se é possível formar um triângulo
    if r1 == r2 and r2 == r3:  # Verificando qual tipo de triângulo é possível formar
        print('Essas retas podem formar um triângulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Essas retas podem formar um triângulo Isósceles')
    else:
        print('Essas retas podem formar um triângulo Escaleno')
else:
    print('Essas retas não formam um triângulo')  # Else para caso não seja possível formar um triângulo
