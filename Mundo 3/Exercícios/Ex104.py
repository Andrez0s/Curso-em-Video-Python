# Crie um programa que tenha uma função leiaint(), que vai funcionar de forma semelhante à função input
# só que fazendo a validação para aceitar apenas um valor numérico

def leiaint(num):
    ok = False
    valor = 0
    while True:
        n = input(num)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO, digite um número válido')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
