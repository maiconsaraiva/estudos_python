"""
Doctests

Para rodar o teste, usamos o comando abaixo:
python -m doctest -v nome_arquivo.py

Obs:
- Dentro do doctest, o Python não reconhece string com aspas duplas, tem que ser aspas simples.
- Se houver espaço em branco no retorno da função no doctest, o resultado poderá não ser o esperado.
    Ex:
    def verdadeiro():
        ###
        # >>> verdadeiro()
        # True   << Note que aqui temos dois espaços em branco. O teste irá falhar mesmo quando deveria passar.
        ###
    return True

# Exemplo:

def soma(a, b):
    #Soma os números a e b

    #>>> soma(1, 2)
    3

    #>>> soma(4, 6)
    10
    #
    return a + b

"""


# Outro Exemplo, aplicando o TDD
def duplicar_valores_na_lista(valores):
    """Duplica os valores em uma lista

    >>> duplicar_valores_na_lista([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar_valores_na_lista([])
    []

    >>> duplicar_valores_na_lista(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar_valores_na_lista([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
    """
    return [n * 2 for n in valores]


# print(duplicar_valores_na_lista([]))


