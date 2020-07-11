"""
zip -> Cria um iterável, chamado "zip object" os elementos de mesma posição cada um dos iteráveis passados como
entrada, juntando-os em uma tupla.

Essa função pode ser um pouco confusa.
"""

# Exemplos
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)  # <zip object at 0x7f28a849d9c0>

print(list(zip1))  # [(1, 4), (2, 5), (3, 6)]
print(list(zip1))  # []
# Assim como o generator e outros objetos, depois que acessamos um objeto zip, ele é limpo da memória automaticamente.


# Sempre podemos gerar uma Lista, Tupla, Set ou Dictionary
zip1 = zip(lista1, lista2)
print(tuple(zip1))  # ((1, 4), (2, 5), (3, 6))

zip1 = zip(lista1, lista2)
print(set(zip1))  # {(2, 5), (1, 4), (3, 6)}

# No caso do dict, o zip, pega o elemento do primeiro iterável, e usa como chave, e do segundo fica como valor.
zip1 = zip(lista1, lista2)
print(dict(zip1))  # {1: 4, 2: 5, 3: 6}

# Outro detalhes é que no caso de dict, só podem ser passados 2 iteráveis, um representando a chave, e outro o valor
lista3 = [7, 8, 9]
# print(dict(zip(lista1, lista2, lista3)))
# ValueError: dictionary update sequence element #0 has length 3; 2 is required

"""
Iteráveis com números diferentes de elementos:
- Os iteráveis precisam ter a mesma quantidade de elementos, caso contrário, para aquele que tiver mais elementos,
  os elementos adicionais serão ignorados.
- O ZIP sempre vai para a junção assim que o iterável com menos elementos acabar, ou seja, ele toma como base o
  iterável com menos elementos.
"""
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9, 10, 11]
print(list(zip(lista1, lista2, lista3)))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# No exemplo acima o "10" foi ignorado.


"""
Usando o zip com diferentes iteráveis
"""
print(list(zip([1, 2, 3], (4, 5, 6), 'ABC', {'a': 20, 'b': 30, 'c': 40})))
# [(1, 4, 'A', 'a'), (2, 5, 'B', 'b'), (3, 6, 'C', 'c')]

print(list(zip([1, 2, 3], (4, 5, 6), 'ABC', {'a': 20, 'b': 30, 'c': 40}.values())))
# [(1, 4, 'A', 20), (2, 5, 'B', 30), (3, 6, 'C', 40)]

# Usando uma tupla, fazendo o desempacotamento antes.

# sem desempacotar
dados = [(0, 1), (2, 3), (4, 5)]
print(list(zip(dados)))  # [((0, 1),), ((2, 3),), ((4, 5),)]

# desempacotando
print(*dados)  # (0, 1) (2, 3) (4, 5)
print(list(zip(*dados)))  # [(0, 2, 4), (1, 3, 5)]

