galera = [['João', 19, 'oi'], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][2])
print('------Separando testes---------')

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')

print('------Separando testes---------')
pessoas = []
dado = []
maior_idade = 0
menor_idade = 0
for p in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])
    dado.clear()
for p in pessoa:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maior_idade += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor_idade += 1
print(f'Temos {maior_idade} maiores e {menor_idade} menores de idade')
