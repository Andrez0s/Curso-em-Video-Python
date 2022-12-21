# Leia nome, idade e sexo de 4 pessoas, no final deve mostrar a média de idade das 4 pessoas, qual o homem mais velho
# quantas mulheres tem menos de 20 anos

# Declaração de variáveis

soma_idades = 0
idade_mais_velho = 0
mulheres_menos_20anos = 0
homem_velho = ''

for i in range(4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo M ou F: ').lower()
    print('-'*30)
    soma_idades += idade  # somando as idades
    if sexo == 'm' and idade > idade_mais_velho:  # Verificando se é homem e se é mais velho que o anterior
        homem_velho = nome
        idade_mais_velho = idade
    elif sexo == 'f' and idade <= 20:  # Verificando se é mulher com 20 anos ou menos
        mulheres_menos_20anos += 1  # Realizando a contagem de quantas mulheres com menos de 20 anos foram cadastradas

if homem_velho == '':  # Verificando se existe pelo menos 1 homem no grupo
    print('Não existe nenhum homem nesse grupo')
else:
    print(f'Homem mais velho é o {homem_velho} com {idade_mais_velho} anos')

if mulheres_menos_20anos == 0:  # Verificando se existem mulheres com menos de 20 anos
    print('Não existe nenhumq mulher nesse grupo')
else:
    print(f'Existem {mulheres_menos_20anos} mulheres com menos de 20 anos')
print(f'A média das idades é {soma_idades / 4}')
