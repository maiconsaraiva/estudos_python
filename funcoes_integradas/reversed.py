"""
Reversed

Obs:
- Não confunda com a função reversed que estudamos na aula sobre Listas.
- A função reverse() só funciona em listas. Já a função reversed() funciona em qualquer iterável
- Ela basicamente reverte (inverte) os valores do iterável, e diferente da função reverse() da Lista, a reversed()
  Não altera o objeto original, apenas gera um novo objeto.

- Retorna um objeto do tipo List Reverse Iterator
"""

# Exemplos
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)  # <list_reverseiterator object at 0x7fc211ec6520>
print(list(res))  # [5, 4, 3, 2, 1]

tupla = (1, 2, 3, 4, 5)
print(tuple(reversed(tupla)))  # (5, 4, 3, 2, 1)

# Conjunto (Set)
print(set(reversed(tupla)))  # {1, 2, 3, 4, 5}
# Observe que o set acima não funcionou o reversed(). Isso por que, em conjuntos não há definição da ordem dos
# elementos.

# Podemos iterar sobre um objeto list_reverseiterator
res = reversed(lista)
for valor in res:
    print(valor, end=',')  # 5,4,3,2,1,

