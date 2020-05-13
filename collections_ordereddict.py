"""
Módulo Collections - Ordered Dict
https://docs.python.org/3.8/library/collections.html#ordereddict-objects

Em um dicionário a ordem de inserção dos elementos não é garantida. Ou seja, mesmo que você crie elementos seguindo uma
ordem alfabética, não há garantia que eles estarão ordenados lá dentro.

O Ordered Dict vem para suprir essa necessidade. Ele é um dicionário como um Dict clássico, porém ele garante a
ordenação dos elementos tal como foram criados.

Obs: O Ordered Dict não ordena automáticamente os elementos, ele apenas respeita a ordem exata de criação pelo usuário,
     e também tem funções para reordenar um elemento. Exemplo: OrderedDict.move_to_end('b')
     (mais detalhes como esse podem ser consultados na documentação.)
"""

# Import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave: {chave}. Valor: {valor}')

"""
Comparando se dois dicionários são iguais.
"""
# Dict comum
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # Resultado: True. 
# O resultado é True por que no dict comum a ordem não importa, então ele entende que são iguais.

# OrderedDict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # Resultado: False (sim, aqui ele entende que são elementos diferentes, por que a ordem importa)

