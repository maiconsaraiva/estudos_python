"""
List Comprehension

- Não existe em outras linguagens de programação.

- Utilizando List Comprehension, nós podemos gerar novas listas com dados processados a partir de outro iteravel.

# Sintaxe da List Comprehension
[ dado for dado in iteravel ]
"""

# Exemplos
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(type(res))  # list
print(res)  # [10, 20, 30, 40, 50]


"""
Para entender melhor o que está acontecendo, devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""

# Exemplo com divisão
res = [numero / 2 for numero in numeros]
print(res) # [0.5, 1.0, 1.5, 2.0, 2.5]

# Exemplo usando uma função


def funcao_x(valor):
    """
    Calcula o quadrado de uma função
    :param valor: Valor a ser elevado ao quadrado
    :return: valor elevado ao quadrado
    """
    return valor * valor


res = [funcao_x(numero) for numero in numeros]
print(res)  # [1, 4, 9, 16, 25]

"""
List Comprehension vs Loop

Vamos entender o poder do List Comprehension, fazendo o mesmo trabalho em um Loop comum
"""

numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)  # [2, 4, 6, 8, 10]

# List Comprehension
print([numero * 2 for numero in numeros])  # [2, 4, 6, 8, 10]


"""
Outros exemplos
"""

# 1
nome = 'Maicon Saraiva'
print([letra.upper() for letra in nome])  # ['M', 'A', 'I', 'C', 'O', 'N', ' ', 'S', 'A', 'R', 'A', 'I', 'V', 'A']


# 2
def caixa_alta(nome: str):
    return nome.title()


amigos = ['miqueias', 'rafael', 'weslley', 'davidson', 'mibson']  # ['Miqueias', 'Rafael', 'Weslley', 'Davidson', 'Mibson']

print([caixa_alta(nome) for nome in amigos])

# Usando um range
print([numero for numero in range(1, 9)])  # [1, 2, 3, 4, 5, 6, 7, 8]


# Convertendo valores e tipos de uma lista para boolean
print([bool(valor) for valor in ['0', 0, '1', 1, [], False, True, 2.5, 3.14, 10]])
# [True, False, True, True, False, False, True, True, True, True]

# Convertendo inteiros para string
print([str(numero) for numero in numeros])  # ['1', '2', '3', '4', '5']



