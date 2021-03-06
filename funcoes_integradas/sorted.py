"""
Sorted

Como o próprio nome já diz, o sorted() serve para ordenar os dados de um iterável.

Obs:

- Apesar do nome parecido com a função sort() que já vimos antes na aula sobre Listas, a função integrada do python
  sorted() é funciona em qualquer iterável, enquanto a sort() funciona apenas em listas.

- Ele não altera o iterável original, apenas gera uma nova lista com os dados de forma ordenada.

- IMPORTANTE: O sorted() sempre retornará uma lista com os dados alterados. Independente de qual o iterável que foi
  usado.
  Porém, é possível converter o resultado, de volta ao formato original.

"""

# Exemplo de sort(), função exclusiva para listas
numeros = [6, 1, 8, 2]
# A função sort(), modifica a própria lista, ordenando os números lá dentro.
numeros.sort()
print(numeros)  # [1, 2, 6, 8]


# Exemplo com o sorted()
numeros = [6, 1, 8, 2]
print(sorted(numeros))  # [1, 2, 6, 8]
# Ordenando de forma decrescente
print(sorted(numeros, reverse=True))  # [8, 6, 2, 1]

# A lista original continua intacta
print(numeros)  # [6, 1, 8, 2]


# Exemplo do sorted em uma tupla
letras = ('A', 'Z', 'H', 'B')
print(sorted(letras))  # ['A', 'B', 'H', 'Z']

# Como falado nas observações, o resultado do sorted() sempre será uma lista, mas se necessário, podemos
# converter o resultado para o formato inicial novamente, a exemplo da tupla.
tupla = tuple(sorted(letras))
print(tupla)  # ('A', 'B', 'H', 'Z')


"""
Podemos usar o sorted para coisas mais complexas
"""
usuarios_twitter = [
    {'name': 'Glenda', 'tweets': ['Meu primeiro Tweet', 'Meu segundo Tweet']},
    {'name': 'Maicon', 'tweets': ['Eu já tinha uma conta no tweeter', 'Por isso, já tenho mais de 100 tweets']},
    {'name': 'Glauber', 'tweets': []},
    {'name': 'Márcio Saraiva', 'tweets': ['Outro tweet']},
    {'name': 'Iêda', 'tweets': []}
]

# Se tentarmos ordenar o dictionary acima com o sorted() dará erro.
# print(sorted(usuarios_twitter))  # TypeError: '<' not supported between instances of 'dict' and 'dict'

# Precisa passar o parâmetros "key"
# Usamos um lambda para calcular a quantidade de tweets do usuário e ordenar por ela (do maior para o menor)
print(sorted(usuarios_twitter, key=lambda usuario: len(usuario['tweets']), reverse=True))


# Ordenando as bandas com musicas mais escutadas
bandas = [
    {'nome': 'Calcinha Preta', 'tocou': 150},
    {'nome': 'Link Park', 'tocou': 120},
    {'nome': 'Fala Mansa', 'tocou': 10},
    {'nome': 'Evanescence', 'tocou': 80},
    {'nome': 'Weslley Safadão', 'tocou': 30},
    {'nome': 'Luxuria', 'tocou': 20},
    {'nome': 'Limão com Mel', 'tocou': 45},
]

# Top 3 bandas
# ToDo: Essa extração dava pra ser feita com o filter também?
top_3 = sorted(bandas, key=lambda banda: banda['tocou'], reverse=True)[:3]

# Imprime
print('Top 3 bandas:')

for banda in top_3:
    print(f'{banda["nome"]}, tocou: {banda["tocou"]}')

# dá pra fazer com list comprehension também:
[print(f'{banda["nome"]}, tocou: {banda["tocou"]}') for banda in top_3]








