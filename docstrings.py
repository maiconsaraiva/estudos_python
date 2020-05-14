"""
   Documentando funções com Docstrings
"""


# Exemplo simples de documentação de função
def diz_oi():
    """Uma função simples que retorna a string 'Oi!' """
    return 'Oi!'


# Podemos fazer acesso à documentação usando o help(nome_da_funcao)
help(diz_oi)

# Podemos acessar o conteúdo da documentação usando a função "__doc__"
print(diz_oi.__doc__)


# Documentando os parâmetros e o retorno da função
def exponencial(numero: float, potencia: int = 2) -> float:
    """Calcula o exponencial (potência) de um número.
    Obs: Se "potencia" não for informado, então o default será 2
    (ou seja, irá calcular o quadrado do número)

    :param numero: Número ao qual deseja calcular o exponencial.
    :param potencia: Valor para cálculo do exponencial.
    :return: float -- Retorna o "numero" elevado à "potencia" informada.
    """
    return numero ** potencia
