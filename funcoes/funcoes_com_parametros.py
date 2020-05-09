"""
Funções com parâmetros.

- São funções que recebem parâmetros de entrada, que serão usadas em processamentos feitos dentro delas.

Se a gente pensar em um programa (processamento) qualquer, geralmente temos:
entrada -> processamento -> saida

- Funções podem ter N parâmetros, ou seja, podemos receber em uma função quantos parâmetros forem necessários
  para realizar o processamento desejado.
- Os parâmetros podem ser de qualquer tipo;
- Se informarmos um número errado de parâmetros obrigatórios esperados pela função, teremos a exception TypeError

Diferença entre Parametros e Argumentos
- Parâmetros são variáveis declaradas na definição de uma função
- Argumentos são os valores ou variáveis que passamos como parâmetros ao executar uma função
"""

"""
# Retorna o quadrado de um número passado no parametro
def quadrado(numero):
    return numero * numero  # também poderiamos utilizar: return numero ** 2


 valor = float(input('Informe um número para obter o seu quadrado'))

print(quadrado(valor))
"""


# Exemplo de geração de exception TypeError por informar a quantidade errada de parâmetros
def soma(a, b):
    return a + b


print(soma(1, 1))  # Resultado: 2
# print(soma(1, 1, 1))  # Resultado: Exception: TypeError: soma() takes 2 positional arguments but 3 were given

"""
Quando definimos uma função e especificamos os Tipos dos parâmetros de entrada, se passarmos valores de Tipos 
diferentes do esperado (e que não são compatíveis entre si), será gerada também uma exception TypeError.
"""


def soma2(a: int, b: int):
    return a + b


print(soma2(1, 2))  # Resultado: 3
# print(soma2(1, ''))  # Resultado: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# No exemplo abaixo, embora o parâmetro esperado seja do tipo Int, o Float é compatível e foi aceito normalmente
print(soma2(1, 2.5))  # Resultado: 3.5


"""
Ordem de passagem dos Parâmetros:
- A ordem que passamos os argumentos devem seguir exatamente a ordem esperada como definida nos parâmetros da função.
- Porém se, na passagem de argumentos nós especificarmos o nome do parâmetro ao qual queremos passar, podemos fazer
  em qualquer ordem.
"""


# Exemplo
def nome_completo(nome, sobrenome):
    return nome + ' ' + sobrenome


print(nome_completo('Maicon', 'Saraiva'))  # Resultado: Maicon Saraiva
print(nome_completo('Saraiva', 'Maicon'))  # Resultado: Saraiva Maicon
print(nome_completo(sobrenome='Saraiva', nome='Maicon'))  # Resultado: Maicon Saraiva
