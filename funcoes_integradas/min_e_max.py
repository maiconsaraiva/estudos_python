"""
Min e Max

São funções integradas do Python.

max() -> Retorna o maior valor em um iterável ou em dois ou mais números passados no **args
min() -> Faz o contrário do Max

- Funcionam com lista, tupla, conjunto e dicionario.
- O primeiro parâmetro é do tipo *args, então podemos passar quantos números desejarmos.
"""

# Exemplos
lista = [10, 8, 12, 4, 99, 34, 99, 250, 30, 22]
print(min(lista))  # 4
print(max(lista))  # 250

# É possível passar N elementos no nas funções min e max:
print(min(1, 2, 6))  # 1
print(max(2, 10, 19))  # 19

# Para usar com o dicionário, se não passarmos os valores ele vai executar a função nas chaves dos elementos.
dicionario = {'a': 2, 'b': 10, 'c': 22.7, 'e': 90, 'd': 70}
print(min(dicionario))  # a
print(max(dicionario))  # e

# se quisermos executar sobre os valores, devemos passar o .values()
dicionario = {'z': 25, 'a': 2, 'b': 10, 'c': 22.7, 'e': 90, 'd': 70}
print(min(dicionario.values()))  # 2
print(max(dicionario.values()))  # 90

# Usando o Max em uma lista de nomes, porém, em vez de considerar a ordem alfabética (que seria o padrão),
# vamos avaliar o tamanho de caracteres
nomes = ['Ana Almeida', 'Zulema']
print(max(nomes, key=lambda nome: len(nome)))  # Ana Almeida

# Se tivermos uma lista de dicionários, usamos o parâmetro key para passar um lambda ou uma função que
# faça os devidos tratamentos
bandas = [
    {'nome': 'Calcinha Preta', 'tocou': 150},
    {'nome': 'Link Park', 'tocou': 120},
    {'nome': 'Fala Mansa', 'tocou': 10},
    {'nome': 'Evanescence', 'tocou': 80},
    {'nome': 'Weslley Safadão', 'tocou': 30},
    {'nome': 'Luxuria', 'tocou': 20},
    {'nome': 'Limão com Mel', 'tocou': 45},
]

# Banda mais tocada
print(max(bandas, key=lambda banda: banda['tocou']))  # {'nome': 'Calcinha Preta', 'tocou': 150}
# Banda menos tocada
print(f'Banda menos tocada: {min(bandas, key=lambda banda: banda["tocou"])["nome"]}')  # {"nome': 'Fala Mansa', 'tocou': 10}


