"""
Funções com parâmetros com valores padrões (Default Values)

- Funções onde a passagem de parâmetro é opcional. Geralmente elas tem um valor default, caso não seja passado um valor
- Lembrando que, quando o parâmetro é obrigatório e não é passado, é gerada uma exception TypeError

- Qualquer tipo de dado pode ser utilizado para definir como default de um parâmetro, inclusive funções.

Por que utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis na execução das funções
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;
- Outra vantagem é definir como default um valor que será o mais utilizado em determinado parâmetro.
"""


# Exemplo de função com parâmetro opcional
def exponencial(numero, potencia=2):
    """Calcula o exponencial (potência) de um número.
    Obs: Se "potencia" não for informado, então o default será 2 (ou seja, irá calcular o quadrado do número)
    """
    return numero ** potencia


print(exponencial(3))  # Resultado: 9  (O parâmetro "potencia" não foi informado, por isso foi calculado o seu quadrado)
print(exponencial(3, 2))  # Resultado: 9 (Passamos o parâmetro agora, e seu valor também é 2)
print(exponencial(3, 4))  # Resultado: 81


# Usando uma função como default de um parâmetro
def get_nome_padrao():
    return 'Sismais Tecnologia'


def nome_empresa(nome=get_nome_padrao()):
    return nome


print(nome_empresa('Casa de Carnes'))
print(nome_empresa())  # Resultado: Sismais Tecnologia


# Usando uma variável como default de uma função
empresa_padrao = 'Sismais Tecnologia'


def nome_empresa(nome=empresa_padrao):
    return nome


print(nome_empresa('Casa de Carnes'))
print(nome_empresa())  # Resultado: Sismais Tecnologia


"""
 Usando uma tupla como valor default 
"""
# Dicionário com tuplas que representam a cotação de moedas
dict_cotacoes = dict({
    ('USD', 'BRL'): 5.73,
    ('BRL', 'USD'): 0.17,
    ('EUR', 'BRL'): 6.29,
    ('JPY', 'BRL'): 0.054
})


def cotacao_moeda(de='USD', para='BRL') -> float:
    """ Retorna a cotação da moeda desejada. O default é USD -> BRL (caso não sejam especificadas as moedas)
        de Dollar vs Real Brasileiro.
        Caso a cotação não esteja na lista, gera uma exception através do .get()
        @:return float Valor da cotação
    """
    cotacao = dict_cotacoes.get((de, para))
    if cotacao:
        return cotacao
    else:
        raise IndexError(f'Cotação das moedas {de} -> {para} não estão cadastradas em dict_cotacoes')


print(cotacao_moeda('EUR', 'BRL'))  # Result: 6.29
print(cotacao_moeda())  # Result: 5.73  (O default é a cotação de USD > BRL
print(cotacao_moeda('USD', 'BRL'))  # Result: 5.73
print(cotacao_moeda('BRL', 'USD'))  # Result: 0.17




