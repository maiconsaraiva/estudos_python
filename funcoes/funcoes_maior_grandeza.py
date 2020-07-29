"""
Funções de Maior Grandeza - Higher Order Function - HOF

O que significa?

- Quando uma linguagem de programação suporte o conceito HOF, indica que podemos:
  -- Ter funções que retornam outras funções como resultado;
  -- Passar uma função como argumento para outra função;
  -- Atribuir uma função à uma variável do tipo função;

Obs: Na seção sobre funções nós utilizamos isso.
"""


# Exemplo - Definindo as funções
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def dividir(a, b):
    return a / b


def multiplicar(a, b):
    return a * b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando todas as funções

print(calcular(4, 3, somar))  # 7
print(calcular(4, 3, diminuir))  # 1
print(calcular(4, 3, dividir))  # 1.33333333...
print(calcular(4, 3, multiplicar))  # 12


"""
Nested Functions - Funções Aninhadas

Em Python, assim como outras linguagens, podemos ter funções dentro de funções, que são conhecidas por
Nested Functions, também chamadas de Inner Functions (Funções Internas).

# Exemplo
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai, blz? ', 'Fora daqui ', 'Filho da mãe ', 'Você tá feio hoje hein '))
    return humor() + pessoa


# Testando
print(cumprimento('Maicon'))
print(cumprimento('Glenda'))


# Nested Functions podem acessar o escopo de funções mais externas
from random import choice


# Exemplo de acesso à variável no escopo da função externa (acima de humor())
def cumprimento2(pessoa):
    def humor():
        return choice(('E ai, blz? ', 'Fora daqui ', 'Filho da mãe ', 'Você tá feio hoje hein ')) + pessoa
    return humor()


print(cumprimento2('Maicon'))
print(cumprimento2('Glenda'))
"""





