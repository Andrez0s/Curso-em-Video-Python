# Reescreva a função leiaint() que fizemos no exercício 104, incluindo agora a possibilidade da digitação
# de um número de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('Por favor digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('\nO usuário decidiu não digitar nenhum valor')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('Por favor digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('\nO usuário decidiu não digitar nenhum valor')
            return 0
        else:
            return n


numero = leiaint('Digite um valor inteiro: ')
numero_float = leiafloat('Digite um valor Real: ')
print(f'O valor digitado foi {numero} e {numero_float}')
