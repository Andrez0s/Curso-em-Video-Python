# Leia vários números inteiros, o programa só vai parar quando o usuário digitar o valor 999, no final mostre
# quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag

contagem_num = 0
soma_total = 0
opcao = 0
num = 0

while num != 999:
    num = int(input('Digite um número ou 999 para sair: '))
    if num != 999:
        soma_total += num
        contagem_num += 1
    else:
        break
print(f'Foram digitados {contagem_num} números e a soma de todos eles é {soma_total}')
