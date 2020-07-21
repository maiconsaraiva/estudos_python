"""
Any e All (funções integradas)

all(): Retorna True, se todos os elementos do iterável são verdadeiros, ou ainda se o iterável está vazio.
  O iterável, pode ser uma tupla, um set, ou mesmo uma string (onde iteramos sobre seus caracteres)

  Importante:
    - Um iterável vazio convertido para boolean retorna False. Ex: bool([])
      Mas, o all() reconhece um iterável vazio como True
    - É importante lembrar que string vazia '' e zero 0 também retorna False.
      Obs: O '0' como string não retorna False
"""


print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? R: False (o "0" é False)

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? R: True
print(all((1, 2, 3, 4)))  # Todos os números são verdadeiros? R: True
print(all({1, 2, 3, 4}))  # Todos os números são verdadeiros? R: True

print(all([]))  # R: True (se estiver vazio então o all() retorna True

# verificando se todos os nomes começam com a letra "C"
nomes = ['Carlos', 'Camila', 'caio', 'Cassio', 'Claúdio']

# Usando o list comprehension
print(all([nome[0].title() == 'C' for nome in nomes]))  # R: True
# Obs: mesmo o nome com letra inicial maiuscula retornou como True por que fizemos uso da função title()

# Verificando se todos os números são pares:
numeros = [2, 4, 6, 8, 10, 12]

print(all(numero % 2 == 0 for numero in numeros))  # True (todos os números são pares)

numeros = numeros + [13, 15, 17]
print(numeros)

print(all(numero % 2 == 0 for numero in numeros))  # False (há numeros ímpares na lista)



"""
any(): Retorna True, se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.

"""

# Exemplo 1
print(any([0, 1, 0, 0, False]))  # True

print(any([0, 0, 0, False, '', {}, (), []]))  # False

print(any([1, 1, '1', False, 0, '']))  # True

# Verificando se algum elemento da lista é par

numeros = [1, 3, 5, 7, 55, 105]

print(any([numero % 2 == 0 for numero in numeros]))  # False

numeros.extend([10, 20])

print(any([numero % 2 == 0 for numero in numeros]))  # True (existem numeros na lista que são pares


