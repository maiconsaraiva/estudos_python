"""
Map

- Mapea o de um iterável para dentro de uma função.
  Retorna o objeto do tipo "Map" que contém uma lista com os retornos da função.
  Substitui o laço for, quando precisamos executar uma função para cada item da lista.

- Recebe dois parâmetros:
  1. Uma função
  2. Um iterável (lista, tupla, etc.)
"""
import math


# Função que usaremos no exemplo
def area_circulo(r):
    """Calcula a área de um círculo com raio "r" """
    # Obs: o math.pi é uma constante da biblioteca math que contém a constante PI
    return round(math.pi * (r ** 2), 6)  # Coloquei um round com precisão de 6 para ficar mais legível


# Lista
lista = [3, 4, 5, 6]


# Exemplo convencional
raios = []
for valor in lista:
    raios.append(area_circulo(valor))

print(raios)  # [28.274334, 50.265482, 78.539816, 113.097336]


# Exemplo usando o map

raios2 = map(area_circulo, lista)

# A função map() retorna um objeto do tipo "map object"
print(raios2)  # <map object at ...>
print(type(raios2))  # <class 'map'>

# convertendo o map para object e obtendo os resultados
print(list(raios2))  # [28.274334, 50.265482, 78.539816, 113.097336]


# EXEMPLO de map com Lambda, em uma Lista
raios3 = map(lambda r: round(math.pi * (r ** 2), 6), lista)
print(raios3)  # <map object at ...>
print(list(raios3))  # [28.274334, 50.265482, 78.539816, 113.097336]
print(list(raios3))  # []
# Observação importante sobre a linha acima: A partir do primeiro momento que você extrai as informações do map, usando
# o cast ou loop, a lista é zerada. E ao tentar acessar uma segunda vez, obterá um lista vazia.
# O resultado é destruido depois de acessado.
# Todo: Pesquisar mais a respeito.


"""
Para fixar:
No map, temos dados iteráveis, e temos uma função
Utilizamos a função: map(funcao, dados_iteraveis)

O map irá mapear cada elemento dos dados e aplicar à função.
O retorno será uma lista contendo o resultado retornado da função para cada item do iterável

A função a ser passada pelo map só recebe um parâmetro, e sempre será o valor dentro da lista/tupla/dictionary
"""


# Mais exemplos

# Cidades e Temperaturas (em graus celcius)
cidades = [('Berlin', 29,), ('Cairo', 36), ('Rio de Janeiro', 32), ('Tokyo', 29), ('Los Angeles', 26), ('Egito', 35)]


# Mostrar os dados da temperatura em Fahrenheit
def converte_graus_fahrenheit(grau_celcius: float) -> float:
    """Função para converter Graus Celcius em Fahrenheit"""
    return (grau_celcius * 9/5) + 32


cidades_fahrenheit = map(lambda cidades: (cidades[0], converte_graus_fahrenheit(cidades[1])), cidades)

# Imprimindo os graus em calcius
print(cidades)
# [('Berlin', 29), ('Cairo', 36), ('Rio de Janeiro', 32), ('Tokyo', 29), ('Los Angeles', 26), ('Egito', 35)]

# Imprimindo os graus em fahrenheit
print(list(cidades_fahrenheit))
# [('Berlin', 84.2), ('Cairo', 96.8), ('Rio de Janeiro', 89.6), ('Tokyo', 84.2), ('Los Angeles', 78.8), ('Egito', 95.0)]





