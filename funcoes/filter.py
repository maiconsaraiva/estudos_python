"""
filter()
Serve para filtrar dados em uma coleção

Assim como a função "map" a função "filter" recebe dois parâmetros: uma função e um iterável
E diferente da função "map" na função "filter" o resultado tem que ser sempre True ou False
  - True: o item será adicionado ao filtro
  - False: o item não será adicionado ao filtro
  Há porém uma exceção, que é o uso do None, que serve para limpar itens vazios dentro do iterável:
  Escopo:
  filter(None, dado)
"""

# biblioteca para trabalhar com dados estatísticos
import statistics

# Média dos valores de uma lista
valores = 1, 2, 3, 4, 5, 6

media = sum(valores) / len(valores)
print(media)  # 3.5
# calculando usando a função "mean" (que também calcula a média) e está presente na biblioteca de estatísticas
media = statistics.mean(valores)
print(media)  # 3.5

# Agora vamos filtrar o valores que ficam cima da média de 3.5
resultado = filter(lambda x: x > media, valores)

print(resultado)  # <filter object at 0x00A61E68>
print(list(resultado))  # [4, 5, 6]
print(list(resultado))  # []  - Assim como no "map" após acessar os dados dentro do objeto filter, eles são destruidos


# Outro exemplo: Usando o filter para remover itens vazios da lista
paises = ['', 'Brasil', 'Argentina', 'Japao', '', 'China']
res = filter(None, paises)
print(list(res))  # ['Brasil', 'Argentina', 'Japao', 'China']
# Obs: Cuidado ao usar o none, pois: Por exemplo, se tivesse um elemento 0 na lista, ele também seria
# removido, porque em Python 0 também é assumido como falseÉ  uma questão de convenção da linguagem Python

# Exemplo, sem usar o None
res = filter(lambda pais: pais != '', paises)
print(list(res))  # ['Brasil', 'Argentina', 'Japao', 'China']


# Exemplo mais complexo

usuarios_twitter = [
    {'name': 'Glenda', 'tweets': ['Meu primeiro Tweet', 'Meu segundo Tweet']},
    {'name': 'Maicon', 'tweets': ['Eu já tinha uma conta no tweeter', 'Por isso, já tenho mais de 100 tweets']},
    {'name': 'Glauber', 'tweets': []},
    {'name': 'Márcio Saraiva', 'tweets': ['Outro tweet']},
    {'name': 'Iêda', 'tweets': []}
]

# Filtrar os usuários que estão inativos no Twitter (sem tweets)
usuarios_inativos = filter(lambda usuario: len(usuario['tweets']) == 0, usuarios_twitter)

print(list(usuarios_inativos))  # [{'name': 'Glauber', 'tweets': []}, {'name': 'Iêda', 'tweets': []}]




