"""
Módulo Collections - Named Tuple
https://docs.python.org/3/library/collections.html#collections.namedtuple

Named Tuple -> Diferente da tuplacomum, nesta específicamos um nome para ela e também parâmetros.

É como se criássemos uma classe, contendo um nome e propriedades.

ToDo: Quais os casos de uso onde é vantagem usar uma tupla e não uma classe?


"""
from collections import namedtuple

cachorro_pitbull = namedtuple('raca', 'pitbull')

# Formas de declaração de uma Named Tuple

# Forma 1
declaração = 'dec'
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 (Recomendada)
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
steve = cachorro(idade=2, raca='Lhasa Apso', nome='Steve')
print(steve)

# Acessando os dados de uma tupla
# Forma 1: Via índice
print(steve[0], steve[1], steve[2])

# Forma 2 (recomendada)
print(steve.idade, steve.nome, steve.raca)

# iterando
for n in steve:
    print(n)
