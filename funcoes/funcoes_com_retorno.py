"""
Funções com retorno

Obs:
 - Em Python, quando uma função não retorna nenhum valor, ele retorna sempre "None".
   Ou seja, se tentarmos capturar o retorno de uma função que não retorna nenhum valor, teremos o retorno None.

Sobre ao retorno no Python "return"

- A palavra reservada "return" finaliza a execução da função e retorna o dado desejado;
- Podemos ter mais de um retorno na função;
- Podemos, em uma função, retornar qualquer tipo de dado, ou até mesmo uma classe personalizada;
- Podemos ter em uma função diferentes returns.
- IMPORTANTE: Diferente do Delphi, Nenhum código depois do "return" será executado.
"""

# Especificando o tipo que será retornado na função
dict_cotacoes = dict({
    ('USD', 'BRL'): 5.73,
    ('EUR', 'BRL'): 6.29,
    ('JPY', 'BRL'): 0.054
})


def cotacao_moeda(de, para) -> float:
    """ Retorna a cotação da moeda desejada.
        Caso a cotação não esteja na lista, gera uma exception através do .get()
        @:return float Valor da cotação
    """
    cotacao = dict_cotacoes.get((de, para))
    if cotacao:
        return cotacao
    else:
        raise IndexError('Moedas não estão cadastradas na lista de cotações (dict_cotacoes)')


print(cotacao_moeda('EUR', 'BRL'))  # Result: 6.29


# Exemplo de função com mais de um retorno
def retorna_numeros():
    return 10, 25, 44, 98


num1, num2, num3, num4 = retorna_numeros()
print(num1, num2, num3, num4)

# Vamos exemplificar um retorno condicional usando a função random. Daremos o nome "joga_moeda"

from random import random


def joga_moeda():
    valor = random()  # Por default o radom retorna um valor float entre 0 e 1.
    if valor > 0.5:
        return 'Cara'
    else:
        return 'Coroa'


print(joga_moeda())
