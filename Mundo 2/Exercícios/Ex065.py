# Leia vários números inteiros, ao final mostre a média entre todos os valores digitados e qual foi o maior e o menor
# numero digitado, o programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

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
