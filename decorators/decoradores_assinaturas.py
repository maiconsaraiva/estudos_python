"""
Decoradores com diferentes assinaturas

- A assinatura de uma função é representada pelo seu nome, parâmetros de entrada e retorno
"""


# Relembrando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


# Testando
print(saudacao('Maicon'))  # OLÁ, EU SOU O/A MAICON


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}. Por favor.'


# TypeError: aumentar() takes 1 positional argument but 2 were given
# print(ordenar('Picanha', 'Batata Frita'))

# Para resolver o problema acima, utilizamos um padrão de projeto chamado Decorator Pattern. Que nada mais são do que
# o uso de *args e **kwargs

# Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}. Por favor.'


print(saudacao('Maicon'))  # OLÁ, EU SOU O/A MAICON
print(ordenar('Picanha', 'Batata Frita'))  # OLÁ, EU GOSTARIA DE PICANHA, ACOMPANHADO DE BATATA FRITA. POR FAVOR.


# Podemos também ter Decorators com argumentos
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                raise ValueError(f'Primeiro argumento precisa ser: {valor}')
            return funcao(*args, **kwargs)
        return outra
    return interna


# Ao informar o argumento pizza, estou indicando que ao decorar a função comida, o primeiro parâmetro deverá ser
# obrigatoriamente 'pizza'
@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


# E ao usar o argumento 10 abaixo, estou indicando que o primeiro argumento deverá ser sempre 10
@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando
print(soma_dez(10, 12))  # 22
# print(soma_dez(1, 21))  # ValueError: Primeiro argumento precisa ser 10


print(comida_favorita('pizza', 'churrasco'))  # ('pizza', 'churrasco')
print(comida_favorita('torta', 'churrasco'))  # ValueError: Primeiro argumento precisa ser: pizza
