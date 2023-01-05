pessoas = {'nome': 'André', 'sexo': 'M', 'idade': 24}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.items())  # Imprime as keys e seus valores
print(pessoas.keys())  # Imprime somente as keys
print(pessoas.values())  # Imprime os valores atribuídos as keys
del pessoas['sexo']  # Para apagar determinada Key
for k in pessoas.keys():
    print(k)

#  ----------------------------------------------------------------

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['sigla'])

brasil.append(estado1.copy())  # Para copiar o conteúdo de um dicionário para uma lista

#----------------------------------------------------------------

for estado in brasil:
    for valor in estado.values():
        print(valor, end=' ')
    print()