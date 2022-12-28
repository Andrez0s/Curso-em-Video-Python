# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte, seu programa deverá ler um número entre 0 e 20 e mostrá-lo por extenso.

extenso = (
            'zero', "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
            "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
          )

while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {extenso[numero]}')
    opcao = input('Deseja continuar? S/N ').lower()
    if opcao == 'n':
        break
