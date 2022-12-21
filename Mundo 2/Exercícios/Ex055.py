# Leia o peso de 5 pessoas e no final mostre qual foi o maior e o menor peso lidos

lista = []
for i in range(1, 6):
    lista.append(float(input('Digite o peso: ')))
print(f'O maior peso foi {max(lista)}Kg e o menor peso foi {min(lista)}Kg')
