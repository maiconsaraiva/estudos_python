"""
Entendendo Iterators e Iterables


Iterator:
- Um objeto que pode ser iterado.
- Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada;

Iterable:
- Um objeto que i´ra retornar um iterator quando a função iter() for chamada.
"""

# Iterables (iteráveis):
# São iteráveis, mas não são um iterator
nome = 'Geek'
numeros = [1, 2, 3, 4, 5, 6]
dicionario = {'a': 1, 'b': 2, 'c': 'c', 'd': True}


# Usando um iterável como um iterator
it1 = iter(nome)

print(next(it1))  # G
print(next(it1))  # e
print(next(it1))  # e
print(next(it1))  # k
