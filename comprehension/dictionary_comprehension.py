"""
Dictionary Comprehension

Pense no seguinte:
- Se quisermos cirar uma lista, fazemos:
  lista = [1, 2, 3, 4]
- Se quisermos criar uma tupla, fazemos:
  tupla = (1, 2, 3, 4)  # Ou: tupla = 1, 2, 3, 4
- Se quisermos criar um set (conjunto):
  conjunto = {1, 2, 3, 4}
- Se quisermos criar um dicionário:
  dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
  Sintaxe: {chave : valor}

E como funciona o Dictionary Comprehension:

Sintaxe do Dictionary Comprehension:
{chave:valor for chave, valor in iteravel}


# Exemplo:
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
numeros_ao_quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(numeros_ao_quadrado)  # {'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}


# Exemplo, gerando um dicionário à partir de uma lista, usando o valor da lista como índice,
# e o valor ao quadrado como valor.
numeros = [1, 2, 3, 4, 5]
dicionario = {valor: valor ** 2 for valor in numeros}
print(dicionario)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Se, no exemplo acima, houver elemento repetido na lista, ao converter para um dicionário, os valores não serão
# duplicados. É preciso ter cuidados ao fazer este uso, para não perder dados.
# Veja
numeros = [1, 2, 3, 4, 5, 1, 2]
dicionario = {valor: valor ** 2 for valor in numeros}
print(dicionario)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} - Os elementos repetidos 1 e 2 foram ignorados.


# Exemplo usando chaves extraidas de uma string
chaves = 'abcdef'
numeros = [1, 2, 3, 4, 5, 6]
dicionario = {chaves[i]: numeros[i] for i in range(0, len(chaves))}
print(dicionario)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

"""


# Exemplo com lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)  # {1: 'impar', 2: 'par', 3: 'impar', 4: 'par', 5: 'impar'}
