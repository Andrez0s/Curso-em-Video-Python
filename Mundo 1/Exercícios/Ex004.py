a = input('Digite algo: ')
print(type(a))
print('É um número?', a.isnumeric())
print('É alfaNumérico?', a.isalnum())
print('É alfabético?', a.isalpha())
print('É ascII?', a.isascii())
print('É um dígito?', a.isdigit())
print('É decimal?', a.isdecimal())
print('É minúsculo?', a.islower())
print('É espaço?', a.isspace())
print('É maiúsculo?', a.isupper())
print('Está capitalizada?', a.istitle())