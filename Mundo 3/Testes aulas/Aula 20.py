def soma(primeiro, segundo):
    print(f'A = {primeiro} e B = {segundo}')
    s = primeiro + segundo
    print(f'A soma primeiro + segundo = {s}')


# Programa principal
soma(primeiro=3, segundo=3)
soma(2, 3)


# -----------------------------

def contador(*valores):  # Usando * para desempacotar parâmetros ( sem saber quantos )
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
