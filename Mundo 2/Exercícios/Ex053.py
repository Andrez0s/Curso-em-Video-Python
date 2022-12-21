# Leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

# Sem laço For

#frase = input('Digite uma frase: ').strip()
#palavras = frase.split()
#junto = ''.join(palavras)
#frase_invertida = junto[::-1]
#if junto == frase_invertida:
#    print(f'A frase digitada foi {junto} ao contrário fica {frase_invertida}\nFormando um palíndromo!')
#else:
#    print(f'A frase digitada foi {junto} ao contrário fica {frase_invertida}\nNÃO Formando um palíndromo!')

# Com laço For

frase = input('Digite uma frase: ').strip()
palavras = frase.split()
junto = ''.join(palavras)
frase_invertida = ''
for letra in range(len(junto) - 1, -1, -1):
    frase_invertida += junto[letra]
if frase_invertida == junto:
    print(f'A frase digitada foi {junto} ao contrário fica {frase_invertida}\nFormando um palíndromo!')
else:
    print(f'A frase digitada foi {junto} ao contrário fica {frase_invertida}\nNÃO Formando um palíndromo!')
