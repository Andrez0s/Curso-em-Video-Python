# Leia uma frase e mostre:
frase = input('Digite uma frase: ')
frase = frase.lower().strip()
# Quantas vezes aparece a letra 'a'
print('Sua frase contêm', frase.count('a'), 'letras a')
# Em que posição aparece a letra 'a' pela primeira vez
print('A letra "a" aparece pela primeira vez na posição:', frase.find('a') + 1)
# Em que posição aparece a letra 'a' pela última vez
print('A letra "a" aparece pela última vez na posição:',frase.rfind('a') + 1)
