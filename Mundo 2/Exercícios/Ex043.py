# Leia o peso e altura de uma pessoa, calcule seu IMC e mostre de acordo com a tabela: Abaixo de 18.5 > Abaixo do peso
# Entre 18.5 e 25 > Peso ideal, acima de 25 ate 30 > sobrepeso, acima de 30 até 40 > Obesidade, acima de 40 > mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print(f'Seu IMC é {imc:.1f} Abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print(f'Seu IMC é {imc:.1f} Peso ideal')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC é {imc:.1f} Sobrepeso')
elif imc > 30 and imc <= 40:
    print(f'Seu IMC é {imc:.1f} Obesidade')
else:
    print(f'Seu IMC é {imc:.1f} Obesidade mórbida')
