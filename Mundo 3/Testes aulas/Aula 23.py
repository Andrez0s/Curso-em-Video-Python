try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:  # Mostra qual tipo de erro foi
    print(f'Problema encontrado foi {erro.__class__ }')
except (ValueError, TypeError):  # É possível ter uma mensagem pernsonalizada para cada tipo de erro
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:  # É possível ter uma mensagem pernsonalizada para cada tipo de erro
    print('Não é possível dividir um número por zero!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre!')
