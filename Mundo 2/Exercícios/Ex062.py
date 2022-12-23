# Melhore o exercício 61 perguntando para o usuário se ele quer mostrar mais alguns termos, o programa encerra quando
# ele disser que quer mostrar 0 termos

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Finalizado com {total} termos')
