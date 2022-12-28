num = [1, 3, 5, 2]

num[2] = 3  # Substituindo a posição 2 pelo valor 3
num.append(4)  # Adicionando um valor ao fim da lista
num.sort()  # Colocando a lista em ordem maior > menor ou alfabética
num.sort(reverse=True)  # Colocando em ordem menor > maior ou alfabética decrescente
num.insert(2, 0)  # Insere um valor na posição 2, inserir um valor 0
num.pop(2)  # Sem parâmetro remove o ultimo valor na lista, com parâmetro remove a posição especificada
num.remove(2)  # Remove o primeiro elemento específicado
print(num)
print(len(num))  # Retornando quantos elementos a lista contêm

a = [1, 2, 3, 4, ]
b = a  # Tudo que for alterado em uma lista, alterará as duas
b = a[:]  # Copiando a lista A para a lista B sem criar uma ligação entre elas

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for posicao, valor in enumerate(valores):
    print(f'Na posição {posicao} encontrei o valor {valor}')
print(f'Cheguei ao final da lista.')
