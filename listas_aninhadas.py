"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação possuem uma estrutura de dados chamados de arrays.
  Os arrays podem ser:
  - Unidimensionais
  - Multidimensionais

- No Python não existe arrays, esse papel é feito pelas Listas

- As Listas Aninhadas no Python são como arrays multidimensionais


# Exemplos

lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3
print(lista_de_listas)
print(type(lista_de_listas))


# Como fazemos para acessar os dados?

# Iterando com loops em uma lista aninhada
for indice, lista in enumerate(lista_de_listas):
    print(f'Lista no índice {indice}:')
    for numero in lista:
        print(f'  {numero}')


# Acessando diretamente um elemento no nível 2 da listas

print(lista_de_listas[0][0])  # 1

print(lista_de_listas[2][1])  # 8

# acessando o numero 8 só que na posição de trás pra frente
print(lista_de_listas[-1][-2])  # 8

print('{:#^48}'.format(''))

# Utilizando List Comprehension em Listas Aninhadas
[[print(numero) for numero in lista] for lista in lista_de_listas]

"""


# Outros exemplos

