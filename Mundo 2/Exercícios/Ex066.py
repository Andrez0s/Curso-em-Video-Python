# Leia vários números inteiros, o programa só vai parar quando o usuário digitar o valor 999, no final mostre
# quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag

lista = []
contagem = 0
opcao = 's'

while opcao == 's':
    num_digitado = int(input('Digite um número: '))
    lista.append(num_digitado)
    contagem += 1
    opcao = input('Deseja continuar? S/N ').lower()
print(f'''Você digitou {contagem} números
O maior número digitado foi {max(lista)}
O menor número digitado foi {min(lista)}
A média dos números digitados foi {sum(lista) / len(lista):.2f}
''')
