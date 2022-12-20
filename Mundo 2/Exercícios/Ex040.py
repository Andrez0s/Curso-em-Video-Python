# leia 2 notas de um aluno e calcule sua média, abaixo de 5 - reprovao, entre 5 e 6.9 - recuperação, acima de 7 - aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua média foi {media:.1f} e você está Reprovado!')
elif media >= 5 and media < 7:
    print(f'Sua média foi {media:.1f} e você está de Recuperação!')
else:
    print(f'Sua média foi {media:.1f} e você está Aprovado!!!')
