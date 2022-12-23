# Simule o funcionamento de um caixa eletrônico, no início, pergunte ao usuário qual será o valor inteiro
# a ser sacado e o programa vai informar quantas cédulas de cada valor serão entregues
# considerar cédulas de 50, 20, 10 e 1

valor = int(input('Qual valor você deseja sacar? '))

notas50 = valor // 50
valor = valor % 50
notas20 = valor // 20
valor = valor % 20
notas10 = valor // 10
valor = valor % 10
notas1 = valor

print('Notas R$ 50,00 = ', notas50)
print('Notas R$ 20,00 = ', notas20)
print('Notas R$ 10,00 = ', notas10)
print('Notas R$ 1,00 = ', notas1)
