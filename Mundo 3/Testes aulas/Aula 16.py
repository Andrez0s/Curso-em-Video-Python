lanche = ('Hambúrguer', 'suco', 'pizza', 'pudim')

for comida in lanche:
    print(comida)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))
