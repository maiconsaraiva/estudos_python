"""
Set Comprehension

Declaração de uma lista:
lista = [1, 2, 3, 4, 5]

Declaração de um Set:
set = {1, 2, 3, 4, 5}
"""

# Exemplos:
numeros_set = {num for num in range(1, 7)}
print(numeros_set)  # {1, 2, 3, 4, 5, 6}

# Outro exemplo
numeros_set = {x ** 2 for x in range(10)}
print(numeros_set) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
# Obs: Por que ficaram nesta ordem? R: Por que o tipo "set" (conjuntos) não tem ordenação,
# ele organiza os elementos dentro dele como bem entender.


# Gerando um dicionário com o exemplo acima:
numeros_set = {x: x ** 2 for x in range(10)}
print(numeros_set)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# Gerando um conjunto (set) com letras extraidas de uma palavra
conjunto = {letra for letra in 'Maicon Saraiva'}
print(conjunto)  # {'M', 'v', 'o', 'a', ' ', 'n', 'S', 'i', 'c', 'r'}

