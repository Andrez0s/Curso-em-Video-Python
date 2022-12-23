# Leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F', caso esteja errado peça a digitação novamente

sexo = input('Digite M para masculino ou F para feminino: ').strip().lower()[0]
while sexo not in 'mf':
#while sexo != 'm' and sexo != 'f':
    sexo = input('Opção inválida! Digite M para masculino ou F para feminino: ').strip().lower()[0]
print(f'O sexo digitado foi {sexo}')
