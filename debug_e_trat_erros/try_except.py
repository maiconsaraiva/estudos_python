"""
Try / Except

Serve para capturar erros que podem ser gerados (a depender da entrada do usuário). Feita a captura podemos efetuar,
tratamentos específicos, sem necessariamente parar de funcionar o programa, ou ainda exibindo alguma mensagem
personalizada.

A forma geral mais simples é:
try:
    //Código
except:
   //O que deve ser feito em caso de problemas


# Tratando um erro de forma genérico (sem analisar o tipo de exception)
try:
    print(int('ABC'))
except:
    print('Deu um problema aqui óóóóóóó!')

# IMPORTANTE: A forma genérica de tratamento do erro, por mais que ela trate o erro corretamente não é a melhor forma.
# O ideal é sempre tratar de acordo com o tipo específico do erro.
try:
    print(int('ABC'))
except ValueError as E:
    print('O dado informado não poder ser convertido para inteiro', E)

# Fazendo tratamentos multiplos
try:
    int('ABC')
except ValueError as erro:
    print('Deu erro aqui: ', erro, erro.__class__)
except TypeError as erro:
    print('Deu erro aqui:', erro, erro.__class__)
except:
    print('Captura genérica!')
"""


def pega_valor(dicionario: dict, chave, valor_default):
    """Retorna o valor em um dictionary, pela chave.
     Se não existir retornar o valor passado em "valor_default" """
    try:
        return dicionario[chave]
    except KeyError:
        return valor_default


dicionario = {'a': 1, 'b': 2}
print(pega_valor(dicionario, 'c', 3))  # 3
