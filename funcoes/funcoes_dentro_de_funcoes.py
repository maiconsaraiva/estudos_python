"""
Podemos ter funções dentro de funções

Não é comum, mas existe a possibilidade.
"""


def dados_pessoa():

    def calcula_limite_disponivel():
        valor_devido = 7500
        # return limite_credito - valor_devido
        # Obs: a variável "limite_credito" usada no return acima também funcionaria, ela foi declarada nesta função,
        # e sim na função aicima dela.
        # Sendo assim, como ela também não é uma variável global, eu posso usa-la normalmente dentro desta função
        # "filha", sem precisar usar o "global limite_credito"
        # A forma correta para resolver essa necessidade é usando a palavra reservada do Python "nonlocal"
        # Exemplo:
        nonlocal limite_credito
        return limite_credito - valor_devido

    nome = 'Maicon'
    sobrenome = 'Saraiva'
    limite_credito = 10000
    limite_disponivel = calcula_limite_disponivel()

    print(nome, sobrenome, limite_credito, limite_disponivel)


dados_pessoa()
