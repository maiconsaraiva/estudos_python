"""
Lambdas

- Conhecidas por "Expressões Lambdas", ou simplesmente "Lambdas", são funções sem nome, ou seja, funções anônimas.

- Funções lambda iniciam com "lambda"

- Geralmente usamos as funções lambda, para fazer filtragem e ordenação de dados.
"""


# Exemplo de função comum em Python
def funcao_x(x):
    return 3 * x + 1


print(funcao_x(4))  # 13
print(funcao_x(7))  # 22

# Exemplos: Como a expressão não tem nome, você já inicia ela definido os parâmetros de entrada
lambda x: 3 * x + 1

# E como utilizar a expressão lambda:

# Exemplo usando uma variável que faz referência a uma expressão lambda. Obs: Não é comum se utilizar desta forma.
calc = lambda x: 3 * x + 1

print(calc(4))  # 13
print(calc(7))  # 22

