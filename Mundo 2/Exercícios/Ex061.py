# Leia o primeiro termo e a razão de uma PA, mostrando os primeiros 10 termos da progressão usando while

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
cont = 1

while cont <= 10:
    print(f'{termo} > ', end='')
    termo += razao
    cont += 1
print('Fim')
